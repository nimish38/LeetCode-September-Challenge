from collections import defaultdict
class Solution:
    def minReorder(self, n, connections):
        cnt, graph, roads = 0, defaultdict(list), set()

        for u,v in connections:
            roads.add((u, v))
            graph[u].append(v)
            graph[v].append(u)
        stack = [(0, -1)]
        while stack:
            item = stack.pop()
            if (item[1], item[0]) in roads:
                cnt += 1

            for nei in graph[item[0]]:
                if nei == item[1]:
                    continue
                stack.append((nei, item[0]))


        return cnt

print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))