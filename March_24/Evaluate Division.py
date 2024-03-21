from collections import defaultdict
class Solution:
    def dfs(self, src, dest):
        stack = [(src, -1)]
        while stack:
            item = stack.pop()
            

    def calcEquation(self, equations, values, queries):
        self.graph, i = defaultdict(list), 0
        for u, v in equations:
            self.graph[u].append(values[i])
            self.graph[v].append(1 / values[i])
            i += 1

        res = []
        for u,v in queries:
            if u not in self.graph or v not in self.graph:
                res.append(-1.0)
            elif u == v:
                res.append(1.0)
            else:
                res.append(self.dfs(u, v))

