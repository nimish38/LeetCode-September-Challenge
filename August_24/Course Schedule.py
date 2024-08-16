from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        adj, indegree = defaultdict(list), [0]*numCourses

        def topologicalSort():
            cnt, que = 0, deque()
            for i in range(numCourses):
                if indegree[i] == 0:
                    cnt += 1
                    que.append(i)
            while que:
                node = que.popleft()
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        cnt += 1
                        que.append(neighbor)
            return cnt == numCourses

        for item in prerequisites:
            a, b = item[0], item[1]
            adj[b].append(a)
            indegree[a] += 1
        return topologicalSort()


print(Solution().canFinish(numCourses = 5, prerequisites = [[1,4],[2,4],[3,1],[3,2]]))
