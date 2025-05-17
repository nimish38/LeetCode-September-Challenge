class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        def solve(node):
            if not node:
                return 0
            left, right = solve(node.left), solve(node.right)
            underground = left + right + node.val
            branch = max(left, right) + node.val
            self.maxSum = max(self.maxSum, underground, branch, node.val)
            return max(branch, node.val)
        solve(root)
        return self.maxSum