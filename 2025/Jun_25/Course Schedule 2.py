from collections import defaultdict, deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adjacency, indegree, queue, res = defaultdict(list), [0] * numCourses, deque(), []
        for a, b in prerequisites:
            adjacency[b].append(a)
            indegree[a] += 1
        for _ in range(numCourses):
            if indegree[_] == 0:
                queue.append(_)
                res.append(_)
        while queue:
            node = queue.popleft()
            for nei in adjacency[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    res.append(nei)
        return res if len(res) == numCourses else []