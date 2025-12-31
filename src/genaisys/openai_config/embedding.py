from .openai_setup import init_openai_api


def get_embedding(
        texts: str | list[str],
        model: str = "text-embedding-3-small"
) -> list[list[float]]:
    """Generate embeddings for the given text(s).
    Args:
        texts: A single string or list of strings to embed.
        model: The embedding model to use.

    Returns:
        List of embedding vectors (list of floats).
    """
    # Handle single text input
    if isinstance(texts, str):
        texts = [texts]
    # Clean text by replacing newlines with spaces
    texts = [text.replace("\n", " ") for text in texts]
    client = init_openai_api()
    # Make the API embedding call
    response = client.embeddings.create(input=texts, model=model)
    # Extract embeddings from response
    embeddings = [item.embedding for item in response.data]
    return embeddings # return a list

# Embedding the chunks
def embed_chunks(chunks,
                 # fast and has a lower resource usage
                 embedding_model="text-embedding-3-small",
                 batch_size=1000) -> list[list[float]]:
    embeddings = []
    for i in range(0, len(chunks), batch_size): # start, stop, step
        chunk_batch = chunks[i:i + batch_size] # Select a batch of chunks
        current_embedding = get_embedding(chunk_batch, model=embedding_model)
        # Append the embedding to the final list
        embeddings.extend(current_embedding)
        print(embeddings)
    return embeddings
