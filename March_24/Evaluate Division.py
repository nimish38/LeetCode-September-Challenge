from collections import defaultdict
class Solution:
    def dfs(self, src, dest):
        stack = [(src, -1, 1.0)]
        while stack:
            item = stack.pop()
            for neighbor, val in self.graph[item[0]]:
                if neighbor == dest:
                    return item[2] * val
                elif neighbor == item[1]:
                    continue
                else:
                    stack.append((neighbor, item[0], item[2] * val))
        return -1.0




    def calcEquation(self, equations, values, queries):
        self.graph, i = defaultdict(list), 0
        for u, v in equations:
            self.graph[u].append((v, values[i]))
            self.graph[v].append((u, 1 / values[i]))
            i += 1

        res = []
        for u,v in queries:
            if u not in self.graph or v not in self.graph:
                res.append(-1.0)
            elif u == v:
                res.append(1.0)
            else:
                res.append(self.dfs(u, v))

        return res

print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))