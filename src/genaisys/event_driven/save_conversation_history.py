import json

from IPython.core.display_functions import display
from ipywidgets import HTML

# Function to save conversation history to a file
def save_conversation_history():
    from . import main
    user_histories = main.user_histories
    filename = "conversation_history.json"  # Define the filename
    with open(filename, 'w') as file:
        json.dump(user_histories, file, indent=4)  # Write the user histories dictionary to the file in JSON format
    display(HTML(f"<div style='color: green;'><strong>Conversation history saved to {filename}.</strong></div>"))
