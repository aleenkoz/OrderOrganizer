""" This module holds the API connection, to an AI chatbot agent: gpt-5.4-mini.
This modules sends a cleaned job string to the AI module and requests information 
extraction using a prompt. The information that should be extracted from the job
segment are: stop(site), item, quantity, priority, and time. 
The output of the prompt should be a clear JSON, so it is easily worked on later. """

import os
from openai import OpenAI

#The API key and endpoint are stored as enviroment variables. 
client = OpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    base_url=f"{os.getenv('AZURE_API_BASE')}/openai/v1/"
)

#The prompt communicated to the AI agent. 
def extract_job_info(job_text: str) -> dict:
    prompt = f"""
    You are a logistics parser. Convert the following job text into structured JSON.

    Text: "{job_text}"

    Return JSON with fields:
    - stop: string
    - item: string
    - quantity: string or number
    - priority: High, Medium, or Low
    - when: normalized time expression (ASAP, Tomorrow AM, End of Day, etc.)

    If something is missing, infer it or leave it empty.
    Only return valid JSON.
    """

    response = client.responses.create(
        model=os.getenv("AZURE_API_DEPLOYMENT"), 
        input=prompt
    )

    output = response.output_text
    #Verify that the value returned by the agent is a JSON output. 
    try:
        data = eval(output)
    except Exception:
        data = {"error": "Invalid JSON returned", "raw": output}

    return data

#Test the module. 
if __name__ == "__main__":
    test = "URGENT cement to site D"
    print(extract_job_info(test))
