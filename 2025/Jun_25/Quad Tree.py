class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        n = len(grid)
        def QuadTree(l, r, u, d):
            if l == r and u == d:
                value = True if grid[u][l] else False
                return Node(value, True)
            node = Node()
            height, width = (u + d) // 2, (l + r) // 2
            a =node.topLeft = QuadTree(l, width, u, height)
            b = node.topRight = QuadTree(width + 1, r, u , height)
            c = node.bottomLeft = QuadTree(l, width, height + 1, d)
            d = node.bottomRight = QuadTree(width + 1, r, height + 1, d)
            if a.isLeaf and b.isLeaf and d.isLeaf and c.isLeaf and a.val == b.val == c.val == d.val:
                node.isLeaf, node.val = True, a.val
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None
            return node
        return QuadTree(0, n - 1, 0, n - 1)

x = Solution().construct(grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
                                 [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
print(x)