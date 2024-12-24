
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

        def solve(rowStart, rowEnd, colStart, colEnd):
            if rowStart == rowEnd and colStart == colEnd:
                return Node(grid[rowStart][colStart], True, None, None, None, None)

            tl = solve(rowStart, rowEnd // 2, colStart, colEnd // 2)
            tr = solve(rowStart, rowEnd // 2, (colEnd // 2) + 1, colEnd)
            bl = solve((rowEnd // 2) + 1, rowEnd, colStart, colEnd // 2)
            br = solve((rowEnd // 2) + 1, rowEnd, (colEnd // 2) + 1, colEnd)
            quad = Node(0, False, tl, tr, bl, br)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == bl.val == br.val):
                quad.isLeaf = True
                quad.val = tl.val
            return quad

        return solve(0, n - 1, 0, n - 1)


x = Solution().construct(grid = [[0,1],[1,0]])
print(x)