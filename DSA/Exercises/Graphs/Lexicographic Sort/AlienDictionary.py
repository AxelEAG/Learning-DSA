
# Alien Dictionary
# Given an array of strings words[], sorted in an alien language. 
# Your task is to determine the correct order of letters in this alien language based on the given words. 
# If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules.


# Kahn's Algorithm

# Track presence of every letter
# Track indegree dependencies
# Independent ones (dependencies = 0) go first
# Add them to the queue, remove them from graph, and update relevant dependencies
# Check again for independent ones and repeat until queue empty.
# If graph is not empty, there's a cycle and dictionary is not valid.

from collections import deque

def findOrderKahn(words: list) -> str:
    exists = {c for word in words for c in word} # Check which letters exist
    graph = {c: set() for c in exists}
    indeg = {c: 0 for c in exists}
    order = []

    # Create graph and track dependencies
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        
        # Find first diff char
        j = 0
        while j < minLen and w1[j] == w2[j]:
            j += 1

        # Add dependencies and update graph
        if j < minLen:
            u, v = w1[j], w2[j]

            if v not in graph[u]: 
                graph[u].add(v)
                indeg[v] += 1

        # Check for invalid word order
        elif len(w1) > len(w2):
            return ''
        
    
    # Get initial queue for topological sort
    q = deque([c for c in exists if indeg[c] == 0])

    while q:
        u = q.popleft()
        order.append(u)

        # Remove char from graph, update dependencies
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Check for cycles
    if len(order) != len(exists):
        return ''

    return ''.join(order)




def findOrderDFS(words: list) -> str:
    # Create graph with all connections
    # dictionary of keys (char) and val: set of chars adjacent to it

    # Go through graph, traversing until reaching one without continuation, 
    # Add it to the answer list, and to the answer set so it's not added again
    # Also keep track of which have been passed by, if already there, there's a cycle

    exists = {c for word in words for c in word}
    graph = {c: set() for c in exists}

    # Create graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        
        # Find first diff letter
        j = 0
        while j < minLen and w1[j] == w2[j]:
            j += 1

        if j >= minLen:
            return '' # Invalid word
        
        u, v = w1[j], w2[j]
        if v not in graph[u]:
            graph[u].add(v)
    
    visited = set()
    onstack = set()
    answer = []
            
    def DFS(u: str) -> bool:
        # Check for cycles
        if u in onstack:
            return False
        
        # Check if already processed
        if u in visited:
            return True
        

        visited.add(u)
        onstack.add(u)

        for v in graph[u]:
            if not DFS(v):
                return False
        
        onstack.remove(u)
        answer.append(u)
        return True
        
    
    # DFS through all letters
    for u in exists:
        if u not in visited:
            if not DFS(u):
                return '' # Cycle detected
        
    return "".join(reversed(answer)) # Answer was built from last to first

# Example usage
words = ["baa", "abcd", "abca", "cab", "cad"]
order = findOrderDFS(words)

print(order)
