def run_conversational_agent(uinput, mrole, mcontent, user_role,user_name):
    conversational_agent(uinput, mrole, mcontent, user_role,user_name)

def conversational_agent(initial_user_input, mrole, mcontent, user_role, user_name):
    messages_obj = [{"role": mrole, "content": mcontent}]
    print("Welcome to the conversational agent! Type 'q' or 'quit' to end the conversation.")

    return