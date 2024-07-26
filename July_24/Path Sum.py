class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def calculate(node, currSum):
            if not node.left and not node.right:
                if currSum + node.val == targetSum:
                    return True
                return False
            Left, Right = False, False
            if node.left:
                Left = calculate(node.left, currSum + node.val)
            if node.right:
                Right = calculate(node.right, currSum + node.val)

            return Left or Right
        if not root:
            return False
        return calculate(root, 0)

