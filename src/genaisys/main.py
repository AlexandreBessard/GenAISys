from genaisys.openai_config import make_openai_api_call

def main():
    print("GenAISys initialized")

if __name__ == "__main__":
    mrole = "system"
    mcontent = "You are an expert in geography."
    # Represents what the human says
    user_role = "user"
    uinput = "In which country is located Paris ?"
    response = make_openai_api_call(uinput, mrole, mcontent, user_role)
    print(response)
    session1 = response
    ninput = "Let's continue our dialog "
    uinput = ninput + session1 + " Would it be safe to go there on vacation ? Make a short answer"
    response = make_openai_api_call(uinput, mrole, mcontent, user_role)
    print(response)