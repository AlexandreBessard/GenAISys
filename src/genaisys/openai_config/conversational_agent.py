from .openai_api import make_openai_api_call
from ..utils import cleanse_conversation_log

"""
uinput: Contains the input (User or System)
mrole: Defines the role of the message (user, system...)
mcontent: What we expect the system to be
user_role: Defines the role of the user
user_name: The name of the user
"""
def run_conversational_agent(uinput, mrole, mcontent, user_role,user_name):
    return conversational_agent(uinput, mrole, mcontent, user_role,user_name)

def conversational_agent(initial_user_input, mrole, mcontent, user_role, user_name):
    # print(f"Welcome {user_name} to the conversational agent! Type 'q' or 'quit' to end the conversation.")
    # response = make_openai_api_call(
    #     input=initial_user_input,
    #     mrole=mrole,
    #     mcontent=mcontent,
    #     user_role=user_role
    # )
    # print(f"Assistant: {response}")
    messages_obj = [{"role": mrole, "content": mcontent}] # Represents a list [] which contains 1 dictionary {}
    print("Welcome to the conversational agent! Type 'q' or 'quit' to end the conversation")
    print(messages_obj[0]["content"])
    if initial_user_input:
        print(f'{user_name} : {initial_user_input}')
        messages_obj.append({"role": user_role, "content": initial_user_input})
    # Clean string representation of conversation
    conversation_string = cleanse_conversation_log(messages_obj)
    print(f"conversation_string -> {conversation_string}")
    try:
        agent_response = make_openai_api_call(
            input=conversation_string,
            mrole=mrole,
            mcontent=mcontent, # You are a helpful assistant
            user_role=user_role,
        )
        messages_obj.append({"role": "assistant", "content": agent_response})
    except Exception as e:
        print(f'Error during API call : {e}')
    # Start the conversation loop
    while True:
        user_input = input(f'{user_name} : ')
        if user_input.lower() in ["q", "quit"]:
            print("Exiting the conversation. Goodbye !")
            break
        # Add the user message to the conversation history
        messages_obj.append({"role": user_role, "content": user_input})
        try:
            conversation_string = cleanse_conversation_log(messages_obj)
            agent_response = make_openai_api_call(
                input=conversation_string,
                mrole=mrole,
                mcontent=mcontent,
                user_role=user_role,
            )
            print(f'Assistant: {agent_response}')
            messages_obj.append({"role": "assistant", "content": agent_response})
        except Exception as e:
            print(f"Error during API call: {e}")
        # Save the conversation log to a file
        with open("conversation_log.txt", "w") as log_file:
            log_file.write(
                "\n".join([
                    f"{(user_name if entry['role'] == 'user' else entry['role'])}: {entry['content']}"
                    for entry in messages_obj
                ])
            )
        print("Conversation saved to 'conversation_log.txt'.")
        #print(f"{messages_obj}")
    return messages_obj
