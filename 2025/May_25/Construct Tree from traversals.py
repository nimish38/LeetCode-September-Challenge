class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        ind = inorder.index(val)
        root.left = self.buildTree(preorder[1: ind + 1], inorder[: ind])
        root.right = self.buildTree(preorder[ind + 1: ], inorder[ind + 1:])
        return root