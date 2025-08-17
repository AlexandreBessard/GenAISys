from config.config import settings

def main():
    print("GenAISys initialized")

def call_openai():
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set")
    print(settings.OPENAI_API_KEY)

if __name__ == "__main__":
    main()
    call_openai()