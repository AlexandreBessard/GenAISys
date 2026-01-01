from genaisys import init_openai_api
from genaisys.pinecone_config import get_pinecode_client


# Receives text to embed and sends the embedded text back
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    client = init_openai_api()
    # Convert text to numerical values
    response = client.embeddings.create(input=[text], model=model)
    embedding = response.data[0].embedding
    return embedding