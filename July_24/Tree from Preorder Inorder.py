class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        root = TreeNode(preorder[0])
        i = 0
        while i < len(preorder) and inorder[i] != root.val:
            i += 1
        if i > 0:
            root.left = self.buildTree(preorder[1: i + 1], inorder[:i])
        if i < len(preorder) - 1:
            root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root


x = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print(x)

