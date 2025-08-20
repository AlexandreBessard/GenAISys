from typing import Iterable

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from genaisys.openai_config.openai_setup import init_openai_api


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
    params = {
        "temperature": 0,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    client = init_openai_api()
    response = client.chat.completions.create(messages=messages_obj, model=model, **params)
    return response.choices[0].message.content
