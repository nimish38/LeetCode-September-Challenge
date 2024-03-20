class Solution:

    def dfs(self, node):
        stack = [node]
        while stack:
            parent = stack.pop()

    def minReorder(self, n, connections):
        self.cnt, self.graph = 0, []
        for _ in range(n):
            self.graph.append([0] * n)

        for i in range(n - 1):
            self.graph[connections[i][0]][connections[i][1]] = 1
            self.graph[connections[i][1]][connections[i][0]] = -1
        # self.dfs(0)
        return self.cnt

print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))