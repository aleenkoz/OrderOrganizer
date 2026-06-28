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

def distance(p1, p2):
    """Euclidean distance between two (lat, lon) points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def normalize_stop(stop: str) -> str:
    """
    Convert messy stop names like 'site D' or 'Stop A' into clean keys: 'D', 'A', etc.
    """
    if not stop:
        return ""

    stop = stop.lower().strip()

    # Remove common prefixes
    for prefix in ["site ", "stop ", "station ", "point "]:
        if stop.startswith(prefix):
            stop = stop.replace(prefix, "")

    return stop.upper()

def compute_route(jobs):
    stops = {normalize_stop(job.get("stop")) for job in jobs if job.get("stop")}
    stops = [s for s in stops if s in COORDS]  # ignore unknown stops

    route = ["Warehouse"]
    current = "Warehouse"
    remaining = stops.copy()

    while remaining:
        nearest = min(
            remaining,
            key=lambda s: distance(COORDS[current], COORDS[s])
        )
        route.append(nearest)
        remaining.remove(nearest)
        current = nearest

    route.append("Warehouse")
    return route
