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
    def construct(self, grid):
        n, curr = len(grid), Node(grid[0][0], 0, None, None, None, None)
        if n == 1:
            curr.isLeaf = 1
            return curr

        # split grids
        mid, tl, tr, bl, br = n//2, [], [], [], []
        for i in range(mid):
            left, right = grid[i][:mid], grid[i][mid:]
            tl.append(left)
            tr.append(right)
        for i in range(mid, n):
            left, right = grid[i][:mid], grid[i][mid:]
            bl.append(left)
            br.append(right)

        curr.topLeft = self.construct(tl)
        curr.topRight = self.construct(tr)
        curr.bottomLeft = self.construct(bl)
        curr.bottomRight = self.construct(br)

        if curr.topLeft.isLeaf and curr.topRight.isLeaf and curr.bottomLeft.isLeaf and curr.bottomRight.isLeaf:
            if curr.topLeft.val == curr.topRight.val == curr.bottomLeft.val == curr.bottomRight.val:
                curr.val = curr.topRight.val
                curr.isLeaf = 1
                curr.topLeft = curr.topRight = curr.bottomLeft = curr.bottomRight = None
        return curr

