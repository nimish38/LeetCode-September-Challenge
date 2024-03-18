class Solution:
    def findCircleNum(self, isConnected):
        visited, n = {}, len(isConnected)

        # forming adjacency matrix
        for i in range(n):
            visited[i] = set()
            for j in range(n):
                if i != j and isConnected[i][j] and j not in visited:
                    visited[i].add(j)

        # check transitive
        i = 0
        while i < len(visited):
            j = 0
            adj = list(visited[list(visited.keys())[i]])
            while j < len(adj):
                visited[i] = visited[i].union(visited[adj[j]])
                del visited[adj[j]]
                j += 1
            i += 1
        return len(visited)

print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))