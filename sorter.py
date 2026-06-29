""" Another simple module for using the previously provided 
priority values to resort the job list and orgnize them to start
from highest priority jobs to least priority jobs."""

from prioritizer import score_priority

def sort_jobs(jobs: list) -> list:
    #Place the output of the prioritizer module. 
    def job_score(job):
        if "priority" in job and job["priority"]:
            return score_priority(job["priority"])
        
        return 1
    #Use the integer priority values to reorgnize the jobs list. 
    sorted_jobs = sorted(jobs, key=job_score, reverse=True)
    return sorted_jobs
