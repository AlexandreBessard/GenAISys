from .chat import chat

# Function to handle the submission of the input via Enter key
def handle_submit(sender):
    from . import main
    debug_output = main.debug_output
    user_message = sender.value
    with debug_output:
        print(f"DEBUG: handle_submit called via Enter key with message: '{user_message}'")

    if user_message and user_message.strip():
        with debug_output:
            print(f"DEBUG: Processing message: '{user_message}'")
        sender.value = ""  # Clear the input box
        chat(user_message)
    else:
        with debug_output:
            print("DEBUG: Ignoring empty message")