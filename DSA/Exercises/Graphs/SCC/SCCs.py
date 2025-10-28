
# Strongly Connected Components are vertices that can reach each other from any starting point
# https://www.geeksforgeeks.org/dsa/strongly-connected-components/

# Brute force approach

# For every vertex,
# if it's not in an scc already,
# Check if it can get to every other member it connects to
# And that they can get to it too

# Other ways are Kosaraju's Algorithm and Tarjan's Algorithm

from collections import defaultdict

class GFG():
    # DFS traversal to reach destination
    def dfs(self, curr, dest, adj, vis):
        if curr == dest:
            return True
        
        # Check all vertices
        vis[curr] = True
        for u in adj[curr]:
            if not vis[u] and self.dfs(u, dest, adj, vis):
                return True
        return False
    
    # Checks if there is a path from source to destination
    def hasPath(self, src, dest, adj):
        vis = {v: False for v in adj}
        return self.dfs(src, dest, adj, vis) 

    def findSCC(self, edges: list) -> list:
        vertices = {v for edge in edges for v in edge}

        # Convert edges into adjacency list
        adj = {v: [] for v in vertices}
        for u, v in edges:
            adj[u].append(v)

        # Store which ones are in an SCC
        inSCC = {v: False for v in vertices}
        sccGroups = []

        # Traverse through all edges and check if they are mutually reachable
        for v in adj:
            if not inSCC[v]:
                inSCC[v] = True
                group = [v]
                for u in adj:
                    if not inSCC[u] and self.hasPath(u, v, adj) and self.hasPath(v, u, adj):
                        inSCC[u] = True
                        group.append(u)
                sccGroups.append(group)

        return sccGroups


if __name__ == "__main__":
    obj = GFG()
    edges = [
        [1, 3], [1, 4], [2, 1], [3, 2], [4, 5]
    ]
    ans = obj.findSCC(edges)
    print("Strongly Connected Components are:")
    for x in ans:
        for y in x:
            print(y, end=" ")
        print()