from genaisys.openai_config import check_openai_api_key

def main():
    print("GenAISys initialized")

if __name__ == "__main__":
    main()
    print(check_openai_api_key().api_key)