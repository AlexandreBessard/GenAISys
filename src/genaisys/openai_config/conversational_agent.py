from .openai_api import make_openai_api_call

def run_conversational_agent(uinput, mrole, mcontent, user_role,user_name):
    return conversational_agent(uinput, mrole, mcontent, user_role,user_name)

def conversational_agent(initial_user_input, mrole, mcontent, user_role, user_name):
    print(f"Welcome {user_name} to the conversational agent! Type 'q' or 'quit' to end the conversation.")
    response = make_openai_api_call(
        input=initial_user_input,
        mrole=mrole,
        mcontent=mcontent,
        user_role=user_role
    )
    print(f"Assistant: {response}")
    return response