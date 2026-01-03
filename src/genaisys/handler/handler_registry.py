from handler import handle_with_memory

handlers = [
    (
        lambda msg, instruct, mem, models, user_message, **kwargs: instruct == "None",
        lambda msg, instruct, mem, models, user_message, **kwargs: handle_with_memory(
            msg, user_message,
            files_status=kwargs.get('files_status'),
            instruct=instruct,
            mem=True, # Ensure to retain conversation memory
            models=models
        )
    )
]