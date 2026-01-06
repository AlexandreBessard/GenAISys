from genaisys import make_openai_api_call
from genaisys.machine_learning import machine_learning

def chain_of_thought_reasoning(initial_query):
    mcontent = """
    You are an information extraction assistant.
Your task is to identify and extract the name of the city mentioned in the user's prompt.
Rules:
- Return ONLY the city name.
- If multiple cities are mentioned, return the most relevant one.
- If no city is mentioned, return "Unknown".
- Do NOT add explanations, punctuation, or extra text.
    """
    query = initial_query['content']
    city = make_openai_api_call(query, mcontent=mcontent)
    result_ml = machine_learning.ml_agent(city, "ACTIVITY")
    return result_ml