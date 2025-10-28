# Tarjan's Algorithm to find SCCs in one pass
# assign id to each node as you pass by them and store them on stack
# if get back to a seen id, that's an scc. Update low index with lowest id and remove them from stack
# Continue process with rest


def tarjan(edges: list) -> list:
    # Create adj list
    vertices = {v for edge in edges for v in edge }
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)

    # Tarjan Bookkeeping
    index = {v: -1 for v in vertices}         # discovery index. -1 = not visited
    lowlink = {v: 0 for v in vertices}        # smallest reachable index
    on_stack = set()
    stack = []
    SCCs = []
    
    counter = [0]

    # DFS through the nodes, updating low-indexes as needed
    def DFS(at):
        idx = counter[0]
        index[at] = lowlink[at] = idx
        counter[0] += 1
        
        on_stack.add(at)
        stack.append(at)

        # Explore all unvisited adjacent nodes
        for to in graph[at]:
            if index[to] == -1: # not visited
                DFS(to)

            # Update low-index if part of SCC
            if to in on_stack:
                lowlink[at] = min(lowlink[to], lowlink[at])
        
        # Once done with traversal, update low-indexes if they
        # are part of SCC (start and end at same place)
        if index[at] == lowlink[at]:
            group = []
            while stack:
                node = stack.pop()
                on_stack.remove(node)
                lowlink[node] = index[at]
                group.append(node)
                if node == at: break

            SCCs.append(group)
    
    # Go through graph
    for at in graph:
        if index[at] == -1:
            DFS(at)
    
    return SCCs