class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        adj, st, vis = {}, [], {}
        for pre in prerequisites:
            take, req = pre[0], pre[1]
            if take in adj:
                adj[take].append(req)
            else:
                adj[take] = [req]

        for val in range(numCourses):
            if val not in adj:
                vis[val] = 1

        while len(vis) < numCourses:
            before = len(vis)
            for node in adj:
                if node not in vis:
                    flag = 0
                    for req in adj[node]:
                        if req not in vis:
                            flag = 1
                    if not flag:
                        vis[node] = 1
            if len(vis) == before:
                return False
        return True


print(Solution().canFinish(numCourses = 20, prerequisites =[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
