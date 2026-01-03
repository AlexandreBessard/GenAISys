import json
from pathlib import Path

# Function to save conversation history to separate files per user
def save_conversation_history(user_histories, output_dir=None):
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "conversation_histories"
    else:
        output_dir = Path(output_dir)
    # Create directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    # Save each user's history to a separate JSON file
    for user, history in user_histories.items():
        filename = output_dir / f"{user}_conversation_history.json"
        with open(filename, 'w') as file:
            json.dump(history, file, indent=4)
    return output_dir