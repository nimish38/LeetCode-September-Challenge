class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def preorder(root):
            if root is None:
                return "N"
            return '#' + str(root.val) + preorder(root.left) + preorder(root.right)

        p1 = preorder(root)
        p2 = preorder(subRoot)
        return p2 in p1