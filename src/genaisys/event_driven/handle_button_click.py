from .chat import chat

# Function to handle the submission of the input via Send button
def handle_button_click(button):
    from . import main
    input_box = main.input_box
    debug_output = main.debug_output
    user_message = input_box.value
    with debug_output:
        print(f"DEBUG: handle_button_click called with message: '{user_message}'")

    if user_message and user_message.strip():
        with debug_output:
            print(f"DEBUG: Processing message: '{user_message}'")
        input_box.value = ""  # Clear the input box
        chat(user_message)
    else:
        with debug_output:
            print("DEBUG: Ignoring empty message")