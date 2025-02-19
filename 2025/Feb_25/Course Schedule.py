class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        adj, st = {}, []
        for pre in prerequisites:
            take, req = pre[0], pre[1]
            if take in adj:
                adj[take].append(req)
            else:
                adj[take] = [req]

        for val in range(numCourses):
            if val not in adj:
                st.append(val)