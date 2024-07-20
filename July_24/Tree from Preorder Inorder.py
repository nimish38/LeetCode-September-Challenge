class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        def construct(start, end):
            root, i = TreeNode(preorder[start]), start
            while inorder[i] != root.val:
                i += 1
            if i > start:
                root.left = construct(start, i - 1)
            if i < end - 1:
                root.right = construct(i + 1, end)
            return root

        return construct(0, len(preorder))


x = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print(x)

