def load_and_display_conversation_log() -> list[str]:
    try:
        with open("conversation_log.txt", "r") as log_file:
            conversation_log = log_file.readlines()
    except FileNotFoundError:
        print("conversation_log.txt file not found.")
        return []
    return conversation_log