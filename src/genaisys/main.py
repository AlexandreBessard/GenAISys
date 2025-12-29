from genaisys import run_conversational_agent
from genaisys.utils import load_and_display_conversation_log

def main():
    print("GenAISys initialized")

if __name__ == "__main__":
    main()
    run_conversational_agent(
        uinput="Tell me about New York. Keep it short",
        mrole="system",
        mcontent="You are a helpful and friendly AI assistant.",
        user_role="user",
        user_name="Alex"
    )
    # Display conversation log after session ends
    log = load_and_display_conversation_log()
    for line in log:
        print(line, end="")