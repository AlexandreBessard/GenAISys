from genaisys.querying_functions import get_query_results, display_results


def handle_rag(user_message):
    print("Processing RAG")
    query_text = user_message
    query_results = get_query_results(user_message, "data01")
    qtext, target_id = display_results(query_results)
    print(qtext)
    print("Processed query results:")
    return qtext