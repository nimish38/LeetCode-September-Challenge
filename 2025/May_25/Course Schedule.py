from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj, indeg, nodes = defaultdict(list), [0] * numCourses, numCourses
        for x, y in prerequisites:
            adj[y].append(x)
            indeg[x] += 1
        que = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                que.append(i)
                nodes -= 1
        while que:
            node = que.popleft()
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    que.append(nei)
                    nodes -= 1
        return nodes == 0