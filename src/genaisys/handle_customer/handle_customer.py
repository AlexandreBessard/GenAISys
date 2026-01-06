from genaisys.reason.reason import chain_of_thought_reasoning


def handle_customer(user_message):
    initial_query = user_message
    reasoning_steps = chain_of_thought_reasoning(initial_query)
    return reasoning_steps