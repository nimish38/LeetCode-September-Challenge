from collections import defaultdict, deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        adj, deg, res, que, vis = defaultdict(list), [0] * n , [], deque([]), set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        for i in range(n):
            if deg[i] == 1:
                vis.add(i)
                que.append(i)

        while n > 2:
            for _ in range(len(que)):
                node = que.popleft()
                n -= 1
                for nei in adj[node]:
                    deg[nei] -= 1
                    if nei not in vis and deg[nei] == 1:
                        vis.add(nei)
                        que.append(nei)
        return list(que)

print(Solution().findMinHeightTrees(n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]))