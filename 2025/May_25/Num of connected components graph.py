from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges) -> int:
        adj, cnt, vis = defaultdict(list), 0, [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            vis[node] = True
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei)

        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        return cnt
