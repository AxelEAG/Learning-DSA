# Kosaraju's Algorithm
# Used for finding out whether a directed graph is strongly connected.

# Simplified steps:
# 1. DFS on Original Graph: Record finish times.
# 2. Transpose the Graph: Reverse all edges.
# 3. DFS on Transposed Graph: Process nodes in order of decreasing finish times to find SCCs.

# Algorithm:
# 1. Initialize vertices as not visited
# 2.



# DFS graph, when done, add to stack
# Reverse graph
# DFS graph, if reach a loop, that's a SCC
# pop stack as needed and begin with first next available
# 

class KSJ:
    def dfs(self, v, adj, vis, order):
        vis[v] = True
        for u in adj[v]:
            if not vis[u]:
                self.dfs(u, adj, vis, order)
        order.append(v)

    def isSSC(self, edges: list):
        # Make graph and reversed graph
        vertices = {v for edge in edges for v in edge}
        adj = {v: [] for v in vertices}
        rev = {v: [] for v in vertices}
        for v, u in edges:
            adj[v].append(u)
            rev[u].append(v)
        
        # DFS main graph, tracking finishing order
        order = []
        vis = {v: False for v in vertices}

        for v in adj:
            if not vis[v]:
                self.dfs(v, adj, vis, order)
        
        # Check if they were all visited
        for v in vis:
            if not vis[v]: return False
        
        # DFS reversed graph, grouping the ones on same scc
        scc = []
        rvis = {v: False for v in vertices}
        while order: # Start from first to end
            v = order.pop()
            if not rvis[v]:
                group = []
                self.dfs(v, rev, rvis, group)
                scc.append(group)

        return scc




