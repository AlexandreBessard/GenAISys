# Function to update the display
from IPython.core.display_functions import display, clear_output
from ipywidgets import HTML


def update_display():
    from . import main
    # Create local references
    debug_output = main.debug_output
    conversation_output = main.conversation_output
    active_user = main.active_user
    user_histories = main.user_histories

    with debug_output:
        print(f"DEBUG: update_display() called. Active user: {active_user}")
        print(f"DEBUG: History for {active_user}: {len(user_histories[active_user])} entries")

    with conversation_output:
        clear_output(wait=True)
        # Display conversation history
        for i, entry in enumerate(main.user_histories[main.active_user]):
            with debug_output:
                print(f"DEBUG: Processing entry {i}: {entry['role']}")
            if entry['role'] == 'user':
                display(HTML(
                    f"<div style='text-align: left; margin-left: 20px; color: blue; margin-bottom: 5px;'><strong>{active_user}:</strong> {entry['content']}</div>"))
            elif entry['role'] == 'assistant':
                display(HTML(
                    f"<div style='text-align: left; margin-left: 20px; color: green; margin-bottom: 5px;'><strong>Agent:</strong> {entry['content']}</div>"))