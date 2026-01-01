from .display_result import display_results
from .query_result import get_query_result

# Receives the query, sends the request and returns the response
def query_vector_store(query_text, namespace):
    print("Querying vector store")
    query_result = get_query_result(query_text, namespace)
    print("Processed query results:")
    text, target_id = display_results(query_result)
    return text, target_id