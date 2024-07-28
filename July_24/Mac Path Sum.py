class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root) -> int:
        if not root:
            return 0
        bestSum = float('-inf')

        def solve(node):
            if not node:
                return 0
            leftSum = solve(node.left)
            rightSum = solve(node.right)

            belowPath = leftSum + rightSum + node.val
            singlePath = max(leftSum, rightSum) + node.val
            onlynode = node.val

            bestSum = max(bestSum, belowPath, singlePath, onlynode)
            return max(singlePath, onlynode)

        solve(root)
        return bestSum

a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
a.left, a.right = b, c
print(Solution().maxPathSum(a))