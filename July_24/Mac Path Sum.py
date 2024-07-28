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