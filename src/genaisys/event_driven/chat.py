from IPython.core.display_functions import clear_output, display
from ipywidgets import HTML

from .chat_with_gpt import chat_with_gpt
from .update_display import update_display
from .save_conversation_history import save_conversation_history

# Function to handle user input and optional bot response
def chat(user_message):
    from . import main
    debug_output = main.debug_output
    conversation_output = main.conversation_output
    user_histories = main.user_histories
    active_user = main.active_user
    agent_checkbox = main.agent_checkbox
    with debug_output:
        print(f"DEBUG: chat() called with message: '{user_message}'")

    # Check for exit signal
    if user_message.lower() in ['exit', 'quit']:
        conversation_active = False
        with conversation_output:
            clear_output()
            display(HTML("<div style='color: red;'><strong>Conversation ended. Saving history...</strong></div>"))
            save_conversation_history()
            display(HTML("<div style='color: green;'><strong>History saved. Proceed to the next cell.</strong></div>"))
        return

    # Append user message to the active user's history
    user_histories[active_user].append({"role": "user", "content": user_message})

    with debug_output:
        print(f"DEBUG: Added user message to history. History length: {len(user_histories[active_user])}")

    # Generate bot response if agent_checkbox is checked
    if agent_checkbox.value:
        with debug_output:
            print("DEBUG: Agent checkbox is checked, generating response...")
        try:
            response = chat_with_gpt(user_histories[active_user], user_message)
            with debug_output:
                print(f"DEBUG: Got response from chat_with_gpt: '{response[:100]}...'")
            # Append bot response to the active user's history
            user_histories[active_user].append({"role": "assistant", "content": response})
            with debug_output:
                print(f"DEBUG: Added assistant response to history. History length: {len(user_histories[active_user])}")
        except Exception as e:
            with debug_output:
                print(f"DEBUG: Error generating response: {e}")
            error_response = f"Error: {str(e)}"
            user_histories[active_user].append({"role": "assistant", "content": error_response})
    else:
        with debug_output:
            print("DEBUG: Agent checkbox is NOT checked, skipping response generation")

    # Update display
    with debug_output:
        print("DEBUG: Calling update_display()")
    update_display()