# https://www.geeksforgeeks.org/dsa/eulerian-path-and-circuit/

# Eulerian Path is a path in graph that visits every edge exactly once. 
#     Requires all edges to be part of a single connected component
#     Exactly zero or two vertices can have odd degrees

# Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex. 
#     Zero vertices can have odd degrees
    
# Given an undirected connected graph with v nodes, and e edges, with adjacency list adj. 
# We need to write a function that returns 
#     2 if contains an eulerian cycle, 
#     1 if contains an eulerian path, 
#     0 Otherwise


EULERIAN_CIRCUIT = 2
EULERIAN_PATH = 1

def isEulerCircuit(v: int, adj: list) -> bool:
    m = len(adj)
    present = {node for node in range(m)} # Depends on adj structure, works for this case.
    visited = {node: False for node in present}
    degrees = {node: len(adj[node]) for node in present} # Count degrees for every node

    # Start on first non-zero degree node
    start = next((i for i, neighbors in enumerate(adj) if neighbors), -1)
    if start == -1: return 2     # Trivially Eulerian: No nodes are connected

    # Check if they are all connected
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)
    for node in visited:
        if adj[node] and not visited[node]: # Ignore zero-degree nodes
            return 0
    
    # Count odd degress
    oddCount = sum(deg % 2 for deg in degrees.values())
    
    match oddCount:
        case 0: 
            return EULERIAN_CIRCUIT
        case 2: 
            return EULERIAN_PATH
        case _:
            return 0
        
if __name__ == "__main__":
    v = 5
    adj = [
        [1, 2, 3], 
        [0, 2], 
        [1, 0], 
        [0, 4], 
        [3]
    ]

    print(isEulerCircuit(v, adj))
