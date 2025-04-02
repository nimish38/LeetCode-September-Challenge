class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        self.maxsum = 0

        def solve(node):
            if not node:
                return 0

            leftval, rightval = solve(node.left), solve(node.right)
            downward_path = leftval + rightval + node.val
            one_side_path = max(leftval, rightval) + node.val
            only_root = node.val
            self.maxsum = max(self.maxsum, downward_path, one_side_path, only_root)
            return max(one_side_path, only_root)

        solve(root)
        return self.maxsum


a, b, c, d, e = TreeNode(-10), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right, c.left, c.right = b, c, d, e
print(Solution().maxPathSum(a))