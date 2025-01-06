class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        st = [(root, root.val)]
        while st:
            node, currSum = st.pop()
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
            if node.right:
                st.append((node.right, currSum + node.right.val))
            if node.left:
                st.append((node.left, currSum + node.left.val))
        return False

