class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        left, right = True, True
        if root.left:
            if root.left.val >= root.val :
                return False
            left = self.isValidBST(root.left)

        if root.right:
            if root.right.val <= root.val :
                return False
            right = self.isValidBST(root.right)

        return left and right

# a, b, c = TreeNode(5), TreeNode(4), TreeNode(1)
# a.right, a.left = b, c
# b.left, b.right = TreeNode(3), TreeNode(2)

a, b = TreeNode(0), TreeNode(1)
a.right = b
print(Solution().isValidBST(a))