from query_result import get_query_result

def query_vector_store(query_text, namespace):
    print("Querying vector store")
    query_result = get_query_result(query_text, namespace)