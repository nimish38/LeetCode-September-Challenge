from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        adj, indeg = defaultdict(list), [0]*numCourses

        def BFSTopoSort():
            res, cnt, que = [], 0, deque()
            for i in range(numCourses):
                if indeg[i] == 0:
                    que.append(i)
                    res.append(i)
                    cnt += 1

            while que:
                node = que.popleft()
                for nei in adj[node]:
                    indeg[nei] -= 1

                    if indeg[nei] == 0:
                        que.append(nei)
                        res.append(i)
                        cnt += 1

            if cnt == numCourses:
                return res
            return []

        for item in prerequisites:
            a, b = item[0], item[1]
            adj[b].append(a)
            indeg[a] += 1

        return BFSTopoSort()