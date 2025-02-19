class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        adj, inrecursion, vis = {}, [False]*numCourses, [False]*numCourses
        for pre in prerequisites:
            take, req = pre[0], pre[1]
            if req in adj:
                adj[req].append(take)
            else:
                adj[req] = [take]

        def isCycle(node):
            vis[node], inrecursion[node] = True, True
            for nei in adj[node]:
                if not vis[nei] and isCycle(nei):
                    return True
                elif inrecursion[nei]:
                    return True
            inrecursion[node] = False
            return False

        for i in range(numCourses):
            if not vis[i] and isCycle(i):
                return False
        return True


print(Solution().canFinish(numCourses = 20, prerequisites =[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
