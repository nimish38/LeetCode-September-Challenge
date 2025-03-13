from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        indegree, adjacency, res, que = [0] * numCourses, defaultdict(list), [], deque()
        for a, b in prerequisites:
            indegree[a] += 1
            adjacency[b].append(a)
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
                que.append(i)
        while que:
            out = que.popleft()
            for nei in adjacency[out]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    res.append(nei)
                    que.append(nei)
        if len(res) == numCourses:
            return res
        return []


print(Solution().findOrder(numCourses = 3, prerequisites = [[2,1],[1,0]]))
