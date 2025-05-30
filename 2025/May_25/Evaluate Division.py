from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        n, adj, res = len(equations), defaultdict(list), []
        for i in range(n):
            a, b = equations[i]
            v = values[i]
            adj[a].append((b, v))
            adj[b].append((a, 1/v))

        def dfs(u, v):
            vis, st = set(), [(u, 1)]
            vis.add(u)
            while st:
                node, val = st.pop()
                for nei, dis in adj[node]:
                    if nei == v:
                        return val * dis
                    if nei not in vis:
                        vis.add(nei)
                        st.append((nei, val * dis))
            return -1.0

        for k in range(len(queries)):
            x, y = queries[k]
            if x not in adj or y not in adj:
                res.append(-1.0)
            elif x == y:
                res.append(1.0)
            else:
                res.append(dfs(x, y))
        return res


print(Solution().calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))