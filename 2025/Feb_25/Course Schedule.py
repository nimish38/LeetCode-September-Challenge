from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        adj, indegree = defaultdict(list), [0] * numCourses
        for pre in prerequisites:
            take, req = pre[0], pre[1]
            if req in adj:
                adj[req].append(take)
            indegree[take] += 1

        # def isCycle(node):
        #     vis[node], inrecursion[node] = True, True
        #     if node in adj:
        #         for nei in adj[node]:
        #             if not vis[nei] and isCycle(nei):
        #                 return True
        #             elif inrecursion[nei]:
        #                 return True
        #     inrecursion[node] = False
        #     return False

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

        return topologicalSort()

        # for i in range(numCourses):
        #     if not vis[i] and isCycle(i):
        #         return False
        # return True


print(Solution().canFinish(numCourses = 20, prerequisites =[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
