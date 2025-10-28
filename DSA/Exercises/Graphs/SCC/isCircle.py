
from typing import List
from collections import defaultdict

def isCircle(words: List[str]) -> bool:
    # Create graph
    letters = {c for word in words for c in [word[0], word[-1]]}
    graph = {c: [] for c in letters}
    for word in words:
        s, e = word[0], word[-1]
        graph[s].append(e) # Doesn't have to be unique



    
    # Determine SCCs and if there's only one


    return True