class Solution:
    def dfs(self, node, n):
        stack = [node]
        while stack:
            parent = stack.pop()
            for i in range(n):
                if self.graph[parent][i] == -1 and not self.visited[i]:
                    self.cnt += 1
                    stack.append(i)
                elif self.graph[parent][i] and not self.visited[i]:
                    stack.append(i)


    def minReorder(self, n, connections):
        self.cnt, self.graph, self.visited = 0, [], [False] * n
        for _ in range(n):
            self.graph.append([0] * n)

        for i in range(n - 1):
            self.graph[connections[i][0]][connections[i][1]] = 1
            self.graph[connections[i][1]][connections[i][0]] = -1
        self.visited[0] = True
        self.dfs(0, n)
        return self.cnt

print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))