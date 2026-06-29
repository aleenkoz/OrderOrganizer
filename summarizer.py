"""This module is to generate everything previously learned into a
human-friendly summary. This module also uses gpt-5.4-mini to translate 
the summary into the user's preferred language."""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    base_url=f"{os.getenv('AZURE_API_BASE')}/openai/v1/"
)

def translate_text(text: str, target_language: str) -> str:
    """
    Translate the given text into the target language using Azure OpenAI.
    """
    prompt = f"Translate the following text into {target_language}:\n\n{text}"

    response = client.responses.create(
        model=os.getenv("AZURE_API_DEPLOYMENT"),
        input=prompt
    )

    return response.output_text


def generate_summary(jobs, route, language="English"):
    """
    Produce a friendly summary and translate it if needed.
    """

    if not jobs:
        summary = "No jobs found today. You're all clear."
    else:
        total_jobs = len(jobs)
        top_job = jobs[0]

        summary = (
            f"You have {total_jobs} jobs today.\n"
            f"The most urgent job is delivering {top_job.get('item')} "
            f"to {top_job.get('stop')} ({top_job.get('priority')}, {top_job.get('when')}).\n"
            f"Your recommended visiting order is: {' → '.join(route)}.\n"
            "You're all set. Have a productive day!"
        )

    # If user wants English, return directly
    if language.lower() in ["english", "en"]:
        return summary

    # Otherwise translate
    translated = translate_text(summary, language)
    return translated
