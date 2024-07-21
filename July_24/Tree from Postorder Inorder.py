class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        def construct(start, end):
            if start > end:
                return
            root, i = TreeNode(postorder[self.idx]), start
            self.idx -= 1
            while inorder[i] != root.val:
                i += 1
            root.right = construct(start, i - 1)
            root.left = construct(i, end)
            return root

        self.idx = len(inorder) - 1
        return construct(0, len(inorder) - 1)

x = Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(x.val)