def generate_summary(jobs, route):
    """
    Produce a friendly, human-readable summary of the day's tasks.
    """

    if not jobs:
        return "No jobs found today. You're all clear."

    total_jobs = len(jobs)

    # Highest priority job
    top_job = jobs[0]
    top_stop = top_job.get("stop", "")
    top_item = top_job.get("item", "")
    top_priority = top_job.get("priority", "")
    top_when = top_job.get("when", "")

    # Build summary text
    summary = []

    summary.append(f"You have {total_jobs} job{'s' if total_jobs > 1 else ''} today.")

    summary.append(
        f"The most urgent job is delivering {top_item} to {top_stop} "
        f"({top_priority}, {top_when})."
    )

    # Route summary
    if route:
        summary.append(
            "Your recommended visiting order is: " +
            " → ".join(route)
        )

    summary.append("You're all set. Have a productive day!")

    return "\n".join(summary)
