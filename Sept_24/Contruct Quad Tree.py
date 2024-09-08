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
        n, curr = len(grid), Node(grid[0][0], False, None, None, None, None)
        if n == 1:
            curr.isLeaf = True
            return curr

        # split grids
        curr.topLeft = self.construct()
        curr.topRight = self.construct()
        curr.bottomLeft = self.construct()
        curr.bottomRight = self.construct()

        if curr.topLeft.isLeaf and curr.topRight.isLeaf and curr.bottomLeft.isLeaf and curr.bottomRight.isLeaf:
            if curr.topLeft.val == curr.topRight.val == curr.bottomLeft.val == curr.bottomRight.val:
                curr.val = curr.topRight.val
                curr.isLeaf = True
                curr.topLeft = curr.topRight = curr.bottomLeft = curr.bottomRight = None
        return curr

             