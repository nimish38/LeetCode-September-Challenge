class Solution:
    def __init__(self):
        self.n = 0
        self.graph = []

    def bfs(self, node):
        que = [node]
        while que:
            item = que.pop(0)
            for j in range(self.n):
                if item != j and self.graph[item][j] and not self.visited[j]:
                    que.append(j)
                    self.visited[j] = True

    def dfs(self, node):
        que = [node]
        while que:
            item = que.pop()
            for j in range(self.n):
                if item != j and self.graph[item][j] and not self.visited[j]:
                    que.append(j)
                    self.visited[j] = True

    def findCircleNum(self, isConnected):
        self.n, self.graph, cnt = len(isConnected), isConnected, 0
        self.visited = [False] * self.n

        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(i)
                cnt += 1
        return cnt

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))