from genaisys import run_conversational_agent

def main():
    print("GenAISys initialized")

if __name__ == "__main__":
    run_conversational_agent(
        uinput="Tell me about New York. Keep it short",
        mrole="system",
        mcontent="You are a helpful and friendly AI assistant.",
        user_role="user",
        user_name="Alex"
    )