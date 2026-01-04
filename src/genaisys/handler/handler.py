from genaisys import init_openai_api, make_openai_api_call

def handle_with_memory(history, current_user_message, **kwargs):
    conversation_history = [
        f"{msg['role'].capitalize()}: {msg['content']}"
        for msg in history if "content" in msg
    ]
    combined_history = "\n".join(conversation_history)
    # Get current user message content
    user_content = current_user_message.get("content", "")
    # Append the latest user message to the history
    full_context = f"{combined_history}\nUser: {user_content}" if combined_history else user_content
    # Get model selection
    models = kwargs.get("models", "OpenAI")
    # API call parameters
    mrole = "system"
    mcontent = "You are a helpful assistant."
    user_role = "user"
    if models == "OpenAI":
        task_response = make_openai_api_call(
            input=full_context,
            mrole=mrole,
            mcontent=mcontent,
            user_role=user_role
        )
        print(task_response)
        return task_response
    elif models == "DeepSeek":
        # TODO: Implement DeepSeek API call
        return "DeepSeek model not yet implemented"

    return "No model selected"