# Given an array of strings, the task is to find if the given strings can be chained to form a circle. 
# A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

from collections import defaultdict

def isCircle(strs: list) -> bool:
    # Create graph of all char starts as key and as val 
    # set of all endings of the words that start with it
    # start: { end1 : count, end2: count  }

    # DFS the graph. For every start, recurse from each ending
    # trying to see if you can cover all words and be back at beginning

    # Create graph
    present = {c for string in strs for c in string}
    graph = {c: defaultdict(int) for c in present}
    graph['count'] = 0

    for s in strs:
        start, end = s[0], s[-1]
        graph[start][end] += 1
        graph['count'] += 1
        graph[start]['count'] += 1

    def DFS(u) -> bool:
        if graph['count'] == 0:
            return True
        
        if graph[u]['count'] == 0:
            return False
        
        for v, count in graph[u].items():
            graph['count'] -= 1
            if count > 0:
                graph[u][v] -= 1
                if DFS(v):
                    return True
                graph[u][v] += 1
            graph['count']

    # Go through graph
    for u in graph:
        if u == 'count': continue
        if DFS():
            return True

    return