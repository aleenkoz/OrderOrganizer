"""This module serves as a bonus function. Asumming hypothetical 
coordinates, distances were calculated. Then These distances were used 
to write down a sensible order of visiting. """

import math

# Coordinates for each stop
COORDS = {
    "Warehouse": (26.43, 50.10),
    "A": (26.39, 50.19),
    "B": (26.45, 50.05),
    "C": (26.30, 50.21),
    "D": (26.51, 50.04),
    "H": (26.40, 50.08)
}
#Possible occurring priorities and  their weights
PRIORITY_WEIGHT = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

#Euclidean distance between two (lat, lon) points.
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#Convert messy stop names like 'site D' or 'Stop A' into clean keys: 'D', 'A', etc.

def normalize_stop(stop: str) -> str:
    if not stop:
        return ""

    stop = stop.lower().strip()

    # Remove common prefixes
    for prefix in ["site ", "stop ", "station ", "point "]:
        if stop.startswith(prefix):
            stop = stop.replace(prefix, "")

    return stop.upper()

#Calculate the weighted score
def stop_priority(stop, jobs):
    """Return the priority weight for a given stop based on job priority."""
    for job in jobs:
        if normalize_stop(job.get("stop")) == stop:
            return PRIORITY_WEIGHT.get(job.get("priority"), 1)
    return 1

#Find the route based on the weighted score, start and end at the warehouse. 
def compute_route(jobs):
    valid_stops = set(COORDS.keys())

    # Normalize stops
    stops = {
        normalize_stop(job.get("stop"))
        for job in jobs
        if job.get("stop")
    }

    # Remove invalid stops
    stops = [s for s in stops if s in valid_stops]

    # Remove Warehouse from stops
    stops = [s for s in stops if s != "Warehouse"]

    route = ["Warehouse"]
    current = "Warehouse"
    remaining = stops.copy()

    while remaining:
        nearest = max(
            remaining,
            key=lambda s: (
                stop_priority(s, jobs) * 10
                - distance(COORDS[current], COORDS[s])
            )
        )
        route.append(nearest)
        remaining.remove(nearest)
        current = nearest

    route.append("Warehouse")
    return route


#Test the module. 
if __name__ == "__main__":
    # Sample jobs to test the optimizer
    sample_jobs = [
        {"stop": "site D", "priority": "High"},
        {"stop": "A", "priority": "Medium"},
        {"stop": "H", "priority": "Medium"},
        {"stop": "C", "priority": "Low"}
    ]

    print("Testing priority‑aware route optimizer...\n")

    route = compute_route(sample_jobs)
    print("Generated Route:")
    print(" → ".join(route))