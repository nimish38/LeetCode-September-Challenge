class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


a = TreeNode(3)
a.left = TreeNode(5)
a.right = TreeNode(1)
a.left.left = TreeNode(6)
a.left.right = TreeNode(2)
a.left.right.left = TreeNode(7)
a.left.right.right = TreeNode(4)

print(Solution().lowestCommonAncestor(a, a.left, a.left.right.right).val)