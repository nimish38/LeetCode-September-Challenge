from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegree, adjacency = [0] * numCourses, defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            adjacency[b].append(a)
        