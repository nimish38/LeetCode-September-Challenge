from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegree, adjacency, que, cnt = [0] * numCourses, defaultdict(list), deque(), 0
        for a, b in prerequisites:
            indegree[a] += 1
            adjacency[b].append(a)
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
                cnt += 1
        while que:
            course = que.popleft()
            for nei in adjacency[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
                    cnt += 1
        return cnt == numCourses


print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))

