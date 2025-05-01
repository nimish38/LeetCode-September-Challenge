from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges) -> bool:
        adj, vis = defaultdict(list), set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in vis:
                return False
            vis.add(node)
            for nei in adj[node]:
                if nei != parent and not dfs(nei, node):
                    return False
            return True

        return  dfs(0, -1) and len(vis) == n

print(Solution().validTree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))