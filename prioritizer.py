""" A simple module for giving string priorty values an integer value, 
so that they are sorted later by priority. """

def score_priority(priority_text: str) -> int:

    #The default is a low priority class (1)
    if not priority_text:
        return 1  

    text = priority_text.lower()

    #High priority (3) is indicated by these words. 
    high_keywords = ["urgent", "asap", "immediately", "now", "critical", "priority"]
    if any(word in text for word in high_keywords):
        return 3

    #Medium priority (2) is indicated by these keywords.
    medium_keywords = ["tomorrow", "end of day", "today", "needs", "am", "pm"]
    if any(word in text for word in medium_keywords):
        return 2

    return 1
