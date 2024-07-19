class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder = []):
        root = curr = TreeNode(preorder[0])
        i, j, n = 0, 0, len(preorder)
        while i < n:
            while j < n and inorder[j] != preorder[i]:
                j += 1
            subtree = inorder[i : j]

            i = i + 1
            while i < j:
                if preorder[i] == inorder[i]:
                    
                i += 1

