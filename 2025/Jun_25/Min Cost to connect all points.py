import heapq
from collections import defaultdict


class Solution(object):
    def minCostConnectPoints(self, points):
        n, cost, adj = len(points), 0, defaultdict(list)
        vis = [False] * n

        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                a, b = points[j]
                dist = abs(a- x) + abs(b - y)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        arr = [(0, 0)]
        while n > 0:
            wt, node = heapq.heappop(arr)
            if not vis[node]:
                vis[node] = True
                n -= 1
                cost += wt
                for dist, nei in adj[node]:
                    if not vis[nei]:
                        heapq.heappush(arr, (dist, nei))
        return cost

print(Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))