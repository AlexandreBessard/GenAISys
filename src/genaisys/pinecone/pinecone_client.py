from pathlib import Path
from pinecone import Pinecone

from genaisys import embed_chunks
from genaisys.config.config import settings
from genaisys.pinecone.upsert_to_pinecone import batch_upsert
from genaisys.pinecone_config import get_pinecode_client, get_serverless_spec

# Get the genaisys package directory (1 level up from this file's directory)
PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SCENARIO_CSV_PATH = PACKAGE_ROOT / "scenarios_data" / "scenario.csv"

def initialize_pinecone_api() -> Pinecone:
    if not settings.PINECONE_API_KEY:
        raise RuntimeError('PINECONE_API_KEY not set')
    return Pinecone(api_key=settings.PINECONE_API_KEY)

if __name__ == "__main__":
    print(initialize_pinecone_api().config.api_key)
    file_path = SCENARIO_CSV_PATH
    print(f"CSV path: {file_path}")
    chunks = []
    with open(file_path, 'r') as file:
        next(file) # -> Skip the header file
        chunks = [line.strip() for line in file]

    for i, chunk in enumerate(chunks[:2], start=1):
        print(chunk)
    # Embedding the dataset
    embeddings = embed_chunks(chunks)
    print(f"Embedding length: {len(embeddings)}")
    print(f'First embedding : {embeddings[0]}')
    print(f"Total number of chunks: {len(chunks)}")
    print(f'Number of embeddings: {len(embeddings)}')
    spec = get_serverless_spec(region="us-east-1")
    pinecone = get_pinecode_client()
    print(spec)
    print(pinecone)
    index_name = "genai-v1"
    # Check if index already exist
    if index_name not in pinecone.list_indexes().names():
        pinecone.create_index(name=index_name,
                              dimension=1536, # dimension of the embedding model
                              metric='cosine',
                              spec=spec)
    index = pinecone.Index(index_name)
    print(index.describe_index_stats())
    index_info = pinecone.describe_index(index_name)
    print(index_info)
    print(f"Cloud provider: {index_info.spec.serverless.cloud}")
    print(f"Cloud provider: {index_info.spec.serverless.region}")
    # Generate IDs for each data item
    ids = [str(i) for i in range(1, len(chunks) + 1)]
    print(ids)
    # Prepare data for upsert
    # Build a list of dictionaries
    # {
    #     "id": "1",
    #     "values": [0.12, 0.98, ...],
    #     "metadata": {
    #         "text": "some chunk of text"
    #     }
    # }
    # zip: pair items together: ("chunk 1", embedding1)
    # outer zip: ("1", ("chunk 1", embedding1))
    # Tuple unpacking: for id, (chunk, emb)
    data_for_upsert = [
        {"id": str(id), "values": emb, "metadata": {"text": chunk}}
        for id, (chunk, emb) in zip(ids, zip(chunks, embeddings))
    ]
    batch_upsert(data_for_upsert)
    print(index.describe_index_stats(include_metadata=True))
