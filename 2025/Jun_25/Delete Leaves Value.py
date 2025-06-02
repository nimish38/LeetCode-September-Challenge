class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def removeLeafNodes(self, root, target):
        if not root:
            return None
        root.left, root.right = self.removeLeafNodes(root.left, target), self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root

a, b, c, d = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(2)
a.left, b.left, c.left = b, c, d
x = Solution().removeLeafNodes(a, 2)
print(x)