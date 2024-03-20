class Solution:
    def minReorder(self, n, connections):
        self.cnt, self.visited = 0, [False] * n
        self.visited[0] = True
        stack = [0]
        while stack:
            parent = stack.pop()
            for i in range(n):
                if [i, parent] in connections and not self.visited[i]:
                    self.visited[i] = True
                    stack.append(i)
                elif [parent, i] in connections and not self.visited[i]:
                    self.cnt += 1
                    self.visited[i] = True
                    stack.append(i)


        return self.cnt

print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))