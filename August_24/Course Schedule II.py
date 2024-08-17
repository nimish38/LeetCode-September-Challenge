from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        adj, vis, inrec = defaultdict(list), [False]*numCourses, [False]*numCourses
        self.res, self.cycle  = [], False

        def DFSTopo(u, v, w, r):
            if not v[u]:
                v[u] = w[u] = True

            for nei in adj[u]:
                if w[nei]:
                    self.cycle = True
                    return
                if not vis[nei]:
                    DFSTopo(nei, v, w, r)
            r.append(u)
            w[u] = False

        for item in prerequisites:
            a, b = item[0], item[1]
            adj[b].append(a)
        for i in range(numCourses):
            if not vis[i]:
                DFSTopo(i, vis, inrec, self.res)

        if not self.cycle:
            return self.res[::-1]
        return []


print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))