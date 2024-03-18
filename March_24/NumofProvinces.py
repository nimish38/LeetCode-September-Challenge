class Solution:
    def findCircleNum(self, isConnected):
        visited, n = {}, len(isConnected)

        # forming adjacency matrix
        for i in range(n):
            visited[i] = set()
            for j in range(n):
                if i != j and isConnected[i][j] and j not in visited:
                    visited[i].add(j)
        print(visited)



Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])