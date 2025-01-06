from collections import defaultdict
class Solution:
    def dfs(self, src, dest):
        stack, vis = [(src, 1.0)], set()
        while stack:
            item = stack.pop()
            vis.add(item[0])
            for neighbor, val in self.graph[item[0]]:
                if neighbor == dest:
                    return item[1] * val
                elif neighbor not in vis:
                    stack.append((neighbor, item[1] * val))
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

print(Solution().calcEquation(equations = [["a","b"],["b","c"],["a","c"],["d","e"]], values = [2.0,3.0,6.0,1.0], queries = [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","d"]]))