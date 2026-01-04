from genaisys.handler.handler import handle_with_memory
# Represents a tuple: 1. A condition by checking when the handler should run
# 2. An action if the condition is true
handlers = [
    # Parameters: (history, current_user_message, active_instruction, selected_model)
    (
        # Condition: check if active_instruction is "None"
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: active_instruction == "None",
        # Handler: call handle_with_memory
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: handle_with_memory(
            history,
            current_user_message,
            files_status=kwargs.get('files_status'),
            instruct=active_instruction,
            mem=True,
            models=selected_model
        )
    )
]