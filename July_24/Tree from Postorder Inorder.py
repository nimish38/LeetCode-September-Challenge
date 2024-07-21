class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        def construct(start, end):
            root, i = TreeNode(postorder[self.idx]), start
            self.idx -= 1
            while inorder[i] != root.val:
                i += 1
            root.right = construct(start, i - 1)
            root.left = construct(i, end)
            return root

        self.idx = len(inorder)
        return construct(0, len(inorder))

    