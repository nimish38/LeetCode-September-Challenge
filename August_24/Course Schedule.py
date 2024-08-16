from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        adj, indegree = defaultdict(list), [0]*numCourses
        for item in prerequisites:
            a, b = item[0], item[1]
            adj[b].append(a)
            indegree[a] += 1
        print(adj, indegree)

print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
