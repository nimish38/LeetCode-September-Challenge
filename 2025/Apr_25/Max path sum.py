class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        left, right, self.best = 0, 0, 0

        def solve(node):
            if not node:
                return 0
            leftsum, rightsum = solve(node.left), solve(node.right)
            self.best = max(self.best, node.val + leftsum, node.val + rightsum)
            return self.best

        left, right = solve(root.left), solve(root.right)
        return max(left + right + root.val, left, right, self.best)
