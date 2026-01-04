from genaisys.chat_with_gpt import chat_with_gpt

def chat(history, current_user_message, reasoning_mode, selected_model):
    response = chat_with_gpt(history, current_user_message, reasoning_mode, selected_model)
    return response