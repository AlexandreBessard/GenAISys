from genaisys import run_conversational_agent
from genaisys.openai_config import make_openai_api_call
from genaisys.orchestrator.scenarios import SCENARIOS, get_scenario

if __name__ == "__main__":
    # Teh input contains an indication of what is expected of the generative AI model.
    # input = "Is the following sentence grammatically correct:This aint the right way to talk"
    # mrole = "system"
    # user_role = "user"
    # mcontent = "Follow the instructions in the input"
    # response = make_openai_api_call(input, mrole, mcontent, user_role)
    # print(response)

    # Semantic Textual Similarity Benchmark (STSB)
    # input = "stsb:Sentence 1: This is a big dog. Sentence 2: This dog is very big."
    # mrole = "system"
    # user_role = "user"
    # mcontent = "Follow the instructions in the input"
    # task_reponse = make_openai_api_call(input, mrole, mcontent, user_role)
    # print(task_reponse)
    prompt = 2 # Semantic scenario
    if prompt == 1:
        # Opinion on a movie, implying that a sentiment analysis might interest the user
        input = "Gladiator II is a great movie although I didn't like some of the scenes. I liked the actors though. Overall I really enjoyed the experience."
    if prompt == 2:
        # Second prompt is a fact implying that a semantic analysis might interest the user
        input = "Generative AI models such as GPT-4o can be built into Generative AI Systems. Provide more information."
    if prompt == 3:
        input = "Imagine a simple Market survey for a random product. Keep it short and simple"

    instructions_as_strings = [entry.description for entry in SCENARIOS]
    print(instructions_as_strings)
    # Define the parameters for the function call
    mrole = "system"
    mcontent = "You are an assistant that matches user inputs to predefined scenarios. Select the scenario that best matches the input. Respond with the scenario_number only."
    user_role = "user"
    selection_input = f"User input: {input}\nScenarios: {SCENARIOS}"
    print(selection_input)
    response = make_openai_api_call(selection_input, mrole, mcontent, user_role)
    scenario_number = int(response)
    print("Scenario number: ", scenario_number)
    scenario = get_scenario(scenario_number)
    instruction = scenario.description
    mrole = "system"
    user_role = "user"
    mcontent = instruction
    sc_input = instruction + " " + input
    print(f'sc_input -> {sc_input}')
    task_response = make_openai_api_call(sc_input, mrole, mcontent, user_role)
    print(task_response)

