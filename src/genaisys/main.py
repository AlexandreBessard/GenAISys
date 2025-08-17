from openai import OpenAI
from genaisys.openai import init_openai_api

def main():
    print("GenAISys initialized")

def call_openai() -> OpenAI:
    client = init_openai_api()
    return client

if __name__ == "__main__":
    main()
    print(call_openai().api_key)