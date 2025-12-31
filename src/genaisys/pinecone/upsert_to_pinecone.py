# Upsert function with namespace
from genaisys.pinecone_config import get_pinecode_client
from genaisys.utils.batch_size import get_batch_size

def upsert_to_pinecone(batch, batch_size, namespace="genaisys"):
    """
    Upserts a batch of data to Pinecone under a specified namespace.
    """
    try:
        pinecode = get_pinecode_client()
        index = pinecode.Index("genai-v1")
        index.upsert(vectors=batch, namespace=namespace)
        print(f"Upserted {batch_size} vectors to namespace '{namespace}'.")
    except Exception as e:
        print(f"Error during upsert: {e}")

# Function to upsert data in batches
def batch_upsert(data, namespace="genaisys"):
    pinecone = get_pinecode_client()
    index = pinecone.Index("genai-v1")

    # Check if data already exists in namespace
    stats = index.describe_index_stats()
    if namespace in stats.namespaces and stats.namespaces[namespace].vector_count > 0:
        print(f"Data already exists in namespace '{namespace}'. Skipping upsert.")
        return

    total = len(data)
    i = 0
    while i < total:
        batch_size = get_batch_size(data[i:])
        batch = data[i:i + batch_size]
        if batch:
            upsert_to_pinecone(batch, batch_size, namespace=namespace)
            i += batch_size
            print(f"Upserted {i}/{total} items...")
        else:
            break
    print("Upsert complete.")