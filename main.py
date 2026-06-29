
from preprocessor import preprocess_input
from extracter import extract_job_info
from sorter import sort_jobs
from renderer import render_table
from optimizer import compute_route
from summarizer import generate_summary


def run_pipeline(raw_text: str):
    """
    Full pipeline:
    1. Split raw text into job segments
    2. Extract structured fields using Azure OpenAI
    3. Sort jobs by urgency
    4. Render final table
    """

    print("\n--- PREPROCESSING ---")
    job_segments = preprocess_input(raw_text)
    print(f"Found {len(job_segments)} job segments.")

    print("\n--- EXTRACTING ---")
    extracted_jobs = []
    for segment in job_segments:
        print(f"Processing: {segment}")
        job = extract_job_info(segment)
        extracted_jobs.append(job)

    print("\n--- SORTING ---")
    sorted_jobs = sort_jobs(extracted_jobs)

    print("\n--- FINAL TABLE ---")
    table = render_table(sorted_jobs)
    print(table)

    print("\n--- ROUTE PLAN ---")
    route = compute_route(sorted_jobs)
    print(" → ".join(route))

    print("\n--- SUMMARY ---")
    language = input("What is your preferred language for the summary? ")
    summary = generate_summary(sorted_jobs, route, language)
    print(summary)

    return sorted_jobs


if __name__ == "__main__":
    # Example input text
    raw_text = """3x pipes to site B asap; deliver gloves (2 boxes) +
      1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day"""

    run_pipeline(raw_text)
