
from prioritizer import score_priority

def sort_jobs(jobs: list) -> list:
    def job_score(job):
        if "priority" in job and job["priority"]:
            return score_priority(job["priority"])
        
        return 1

    sorted_jobs = sorted(jobs, key=job_score, reverse=True)
    return sorted_jobs
