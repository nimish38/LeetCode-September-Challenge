class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxval = 0
        def diameter(root):
            if not root:
                return 0
            l, r = 0, 0
            if root.left:
                l = 1 + diameter(root.left)
            if root.right:
                r = 1 + diameter(root.right)
            self.maxval = max(self.maxval, l + r)
            return max(l,r)
        diameter(root)
        return self.maxval


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, b.left, b.right = b, c, d, e
print(Solution().diameterOfBinaryTree(a))