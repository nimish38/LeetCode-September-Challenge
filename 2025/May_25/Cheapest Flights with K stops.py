from collections import defaultdict, deque


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj, distance = defaultdict(list), [float('inf')] * n
        for u, v, c in flights:
            adj[u].append((v, c))
        distance[src], que = 0, deque([(src, 0)])
        while que and k >= 0:
            for _ in range(len(que)):
                node, curr = que.popleft()
                for nei, cost in adj[node]:
                    if curr + cost < distance[nei]:
                        distance[nei] = cost + curr
                        que.append((nei, cost + curr))
            k -= 1
        return -1 if distance[dst] == float('inf') else distance[dst]