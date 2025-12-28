from .openai_setup import init_openai_api

def make_openai_api_call(input: str, mrole: str, mcontent: str, user_role: str):
    model = "gpt-4o"
    messages_obj = [
        {
            "role": mrole, # Set the behavior of the assistant
            "content": mcontent
        },
        {
            "role": user_role,
            "content": input
        }
    ]
    # Define all parameters in a dictionary named params:
    params = { # Python dictionary
        "temperature": 0, # Control the randomness of a response. 0 will produce deterministic response 1, creative
        "max_tokens": 1024, # Limits the token of a response
        "top_p": 1, # Control diversity of the response
        "frequency_penalty": 0, # Reduces the repetition of tokens to avoid redundancies
        "presence_penalty": 0 # Encourages new content by penalizing existing content to avoid redundancies
    }
    client = init_openai_api()
    # **params means take each key/value in the dictionary and pass it as a named argument
    # Equivalent to write:
    # client.chat.completions.create(
    #     messages=messages_obj,
    #     model=model,
    #     temperature=0,
    #     max_tokens=1024,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    response = client.chat.completions.create(messages=messages_obj, model=model, **params)
    return response.choices[0].message.content
