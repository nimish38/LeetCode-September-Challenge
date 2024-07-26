class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def calculate(node, currSum):
            if not node:
                if currSum == targetSum:
                    return True
                return False
            return calculate(node.left, currSum + node.val) or calculate(node.right, currSum + node.val)

        return calculate(root, 0)

