

def score_priority(priority_text: str) -> int:

    if not priority_text:
        return 1  

    text = priority_text.lower()

    high_keywords = ["urgent", "asap", "immediately", "now", "critical", "priority"]
    if any(word in text for word in high_keywords):
        return 3

    medium_keywords = ["tomorrow", "end of day", "today", "needs", "am", "pm"]
    if any(word in text for word in medium_keywords):
        return 2

    return 1
