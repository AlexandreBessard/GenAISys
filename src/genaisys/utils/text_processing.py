import re

def cleanse_conversation_log(messages_obj):
    """
    Converts the conversation log into a single string and removes problematic punctuations.
    """
    conversation_str = " ".join(
        [f"{entry['role']}: {entry['content']}" for entry in messages_obj]
    )
    # Remove problematic punctuations
    return re.sub(r"[^\w\s,.?!:]", "", conversation_str)