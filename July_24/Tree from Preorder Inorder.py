class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        i = 0
        while i < len(preorder) and inorder[i] != root.val:
            i += 1
        root.left = self.buildTree(preorder[1: i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root


#   make first node from preorder as root
#   find that node in inorder
#   recursively call all left nodes in inorder as root.left
# recursively call all right nodes in inorder as root.right
#  repeat till empty

