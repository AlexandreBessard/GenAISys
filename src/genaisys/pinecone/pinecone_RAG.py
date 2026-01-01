from pathlib import Path

from genaisys import embed_chunks
from genaisys.pinecone.upsert_to_pinecone import upsert_to_pinecone, batch_upsert
from genaisys.querying_functions.query_vector_store import query_vector_store
from genaisys.utils.load_file import load_file
from genaisys.openai_config.chunk_text_with_gpt4o import chunk_text_with_gpt4o
from genaisys.pinecone_config import get_pinecode_client, get_serverless_spec

# Get absolute path to resources folder
RESOURCES_PATH = Path(__file__).resolve().parents[2] / "resources"

if __name__ == "__main__":
    print("test")
    file_path = RESOURCES_PATH / "data01.txt"
    text = load_file(file_path)
    chunks = chunk_text_with_gpt4o(text=text)
    print(chunks)
    chunks = chunks.split("\n\n")  # Assume GPT-4o separates chunks with double newlines
    #print(chunks)
    # Display the chunks
    print("Chunks:")
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i + 1}:")
        print(chunk)
    print(f"Total number of chunks: {len(chunks)}")
    # Embedding the chunks
    # Turning words into numbers
    embeddings = embed_chunks(chunks)
    print(f"Number of embeddings: {len(embeddings)}")
    #Pinecone index:
    index_name = "genai-v1"
    namespace = "data01"
    # Generate IDs for each data item
    ids = [str(i) for i in range(1, len(chunks) + 1)]

    # Prepare data for upsert
    data_for_upsert = [
        {"id": str(id), "values": emb, "metadata": {"text": chunk}}
        for id, (chunk, emb) in zip(ids, zip(chunks, embeddings))
    ]
    print(data_for_upsert)
    batch_upsert(data_for_upsert, namespace=namespace)
    pinecone = get_pinecode_client()
    index = pinecone.Index(index_name)
    print(index.describe_index_stats())

    namespace = "genaisys"
    # Retrieve instruction scenario
    query_text = "The customers like the idea of travelling and learning. Provide your sentiment."
    # query_text = "Provide info about new york"
    text, target_id = query_vector_store(query_text, namespace=namespace)
    print("Final output:")
    print(f"Text: {text}")
    print(f"Target ID: {target_id}")

    # Define your namespace and query text
    namespace = "data01"  # Example namespace
    query_text = "What did the CTO say about the different types of memory?"
    # Call the query function
    text, target_id = query_vector_store(query_text, namespace)
    # Display the final output
    print("Final output:")
    print(f"Text: {text}")
    print(f"Target ID: {target_id}")