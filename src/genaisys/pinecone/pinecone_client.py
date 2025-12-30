from pathlib import Path
from pinecone import Pinecone
from genaisys.config.config import settings

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

    print(f"Total number of chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks[:2], start=1):
        print(chunk)
    # Embedding the dataset
    embedding_model = "text-embedding-3-small"
