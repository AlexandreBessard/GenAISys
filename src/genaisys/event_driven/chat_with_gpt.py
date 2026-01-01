import openai

from genaisys import init_openai_api, make_openai_api_call
from genaisys.querying_functions import get_query_result
from genaisys.querying_functions import display_results

def chat_with_gpt(messages, user_message):
    user_memory = True
    try:
      namespace=""
      if "Pinecone" in user_message or "RAG" in user_message:
         # Determine the keyword
        if "Pinecone" in user_message:
            namespace="genaisys"
        elif "RAG" in user_message:
            namespace="data01"
        print(namespace)
        #define query text
        query_text=user_message
        # Retrieve query results
        query_results = get_query_result(query_text, namespace)
        # Process and display the results
        print("Processed query results:")
        qtext, target_id = display_results(query_results)
        print(qtext)
        #run task
        sc_input=qtext + " " + user_message
        mrole = "system"
        mcontent = "You are an assistant who executes the tasks you are asked to do."
        user_role = "user"
        task_response = make_openai_api_call(sc_input,mrole,mcontent,user_role)
        print(task_response)
        aug_output=namespace + ":" +task_response
      else:
        if user_memory:
                # Extract ALL user messages from the conversation history
                user_messages_content = [
                    msg["content"] for msg in messages
                    if msg["role"] == "user" and "content" in msg
                ]

                # Combine all extracted user messages into a single string
                combined_user_messages = " ".join(user_messages_content)

                # Add the current user_message to the combined text
                umessage = f"{combined_user_messages} {user_message}"
        else:
                umessage = user_message
        mrole = "system"
        mcontent = "You are an assistant who executes the tasks you are asked to do."
        user_role = "user"
        task_response = make_openai_api_call(umessage,mrole,mcontent,user_role)
        aug_output=task_response
      # Return the augmented output
      return aug_output
    except Exception as e:
        return f"An error occurred: {e}"