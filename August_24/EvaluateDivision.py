from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        # its a graph solution as equations follow transitivity principle
        adj, i, res = defaultdict(list), 0, []

        def dfs(src, dest, vis, prod):
            if src in vis:
                return
            vis.add(src)
            if src == dest:
                self.ans = prod
                return
            for nei, val in adj[src]:
                dfs(nei, dest, vis, prod * val)

        for item in equations:
            u, v = item[0], item[1]
            val = values[i]
            i += 1
            adj[u].append((v, val))
            adj[v].append((u, 1/val))

        for que in queries:
            src, dest, vis = que[0], que[1], set()
            if src not in adj or dest not in adj:
                res.append(-1.0)
            if src == dest:
                res.append(1.0)
            else:
                self.ans, prod = -1.0, 1.0
                dfs(src, dest, vis, prod)
                res.append(self.ans)

        return res

print(Solution().calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))