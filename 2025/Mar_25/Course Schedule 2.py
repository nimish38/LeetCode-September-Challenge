from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        indegree, adjecancy, res = [0] * (numCourses - 1), defaultdict(list), []
        for a, b in prerequisites:
            adjecancy[a].append(b)
            indegree[a] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
        for a, b in prerequisites:
            indegree[a] -= 1
            if indegree[a] == 0:
                res.append(a)
        if len(res) == numCourses:
            return res
        return []
