""" This module is responsible for
cleaining a messy raw text and 
breaking it down into segments. """

import re

def preprocess_input(text: str) -> list:

    #Unify the conjuction symbol
    normalized = text.replace("+", ";")
    normalized = normalized.replace(",", ";")

    #Split at the conjuctions. 
    raw_segments = normalized.split(";")

    #Clean all the spacing issues, and append to a list of clean jobs
    jobs = []
    for seg in raw_segments:
        seg = seg.strip()

        seg = re.sub(r"\s+", " ", seg)
        seg = seg.replace(" (", "(").replace(") ", ")")

        if seg:  
            jobs.append(seg)

    return jobs

#Test the module
if __name__ == "__main__":
    messy = "3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; " \
    "pickup empty pallets from C; H needs 5 vests by end of day"
    print(preprocess_input(messy))
