from genaisys.handler.handler_registry import handlers

def chat_with_gpt(history, current_user_message, active_instruction, selected_model):
    try:
        for condition, handler in handlers:
            if condition(history, current_user_message, active_instruction, selected_model):
                return handler(history, current_user_message, active_instruction, selected_model)
    except Exception as e:
        return f"An error occured: {str(e)} "