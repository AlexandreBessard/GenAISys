from genaisys.pinecone_config import get_pinecode_client
from genaisys.querying_functions.embedding import get_embedding


# Receives the query, sends it to be embedded, makes the actual query and returns the response
def get_query_results(query_text, namespace):
    # Query converted to numerical data
    query_vector = get_embedding(query_text)
    index_name = "genai-v1"
    pinecone = get_pinecode_client()
    index = pinecone.Index(index_name)
    # Perform the query
    query_results = index.query(
        vector=query_vector,
        namespace=namespace,
        top_k=1,
        include_metadata=True
    )
    return query_results