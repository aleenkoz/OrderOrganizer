import os
from openai import OpenAI

print("API KEY:", os.getenv("AZURE_API_KEY"))
print("BASE URL:", os.getenv("AZURE_API_BASE"))
print("DEPLOYMENT:", os.getenv("AZURE_API_DEPLOYMENT"))

client = OpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    base_url=f"{os.getenv('AZURE_API_BASE')}/openai/v1/"
)


def extract_job_info(job_text: str) -> dict:
    """
    Uses Azure OpenAI Responses API to convert a job segment
    into structured logistics fields:
    stop, item, quantity, priority, when
    """

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

    try:
        data = eval(output)
    except Exception:
        data = {"error": "Invalid JSON returned", "raw": output}

    return data


if __name__ == "__main__":
    test = "URGENT cement to site D"
    print(extract_job_info(test))
