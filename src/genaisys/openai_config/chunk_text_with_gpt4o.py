from openai.types.chat import ChatCompletionSystemMessageParam

from .openai_setup import init_openai_api


def chunk_text_with_gpt4o(
        text: str,
        model: str = "gpt-4o",
        chunk_size: str = "50-100"
) -> str:
    messages: list[ChatCompletionSystemMessageParam] = [
        {
            "role": "system",
            "content": f"You are an assistant skilled at splitting long texts into "
                       f"meaningful, semantically coherent chunks of {chunk_size} words each."
        },
        {
            "role": "user",
            "content": f"Split the following text into meaningful chunks:\n\n{text}"
        }
    ]
    client = init_openai_api()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=1024
    )
    print(response)
    return response.choices[0].message.content
