
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        visited = {}

        def dfs(curr):
            if not node:
                return None

            if curr in visited:
                return visited[curr]

            clone = Node(curr.val, [])
            visited[curr] = clone
            clone.neighbors = [dfs(n) for n in curr.neighbors]

            return clone

        return dfs(node)


a = Node(1, [])
b = Solution().cloneGraph(a)
print(b)