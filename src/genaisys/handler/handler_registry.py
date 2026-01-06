from genaisys.handle_customer.handle_customer import handle_customer
from genaisys.handler.handler import handle_with_memory
from genaisys.rag.handle_rag import handle_rag
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
    ),
    (
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: active_instruction == "RAG",
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: handle_rag(current_user_message)
    ),
    (
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: active_instruction == "Customer",
        lambda history, current_user_message, active_instruction, selected_model, **kwargs: handle_customer(
            current_user_message)
    )
]