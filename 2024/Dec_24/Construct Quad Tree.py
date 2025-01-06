
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> 'Node':
        n = len(grid)

        def solve(row, col, size):
            if size == 1:
                return Node(grid[row][col], True, None, None, None, None)

            tl = solve(row, col, size // 2)
            tr = solve(row, col + size // 2, size // 2)
            bl = solve(row + size // 2, col, size // 2)
            br = solve(row + size // 2, col + size // 2, size // 2 )
            quad = Node(0, False, tl, tr, bl, br)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == bl.val == br.val):
                quad.isLeaf = True
                quad.val = tl.val
                quad.topRight = quad.topLeft = quad.bottomRight = quad.bottomLeft = None
            return quad

        return solve(0, 0, n)


x = Solution().construct(grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
print(x)