from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        # its a graph solution as equations follow transitivity principle

        adj, i = defaultdict(list), 0
        for item in equations:
            u, v = item[0], item[1]
            val = values[i]
            i += 1
            adj[u].append((v, val))
            adj[v].append((u, 1/val))

        

print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))