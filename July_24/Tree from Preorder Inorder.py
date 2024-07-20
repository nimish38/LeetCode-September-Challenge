class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        def construct(start, end, curr):
            root, i = TreeNode(preorder[curr]), start
            for i in range(start, end + 1):
                if inorder[i] == root.val:
                    break
            self.curr += 1
            if i > start:
                root.left = construct(start, i - 1, self.curr)
            if i < end:
                root.right = construct(i + 1, end, self.curr)
            return root

        self.curr = 0
        return construct(0, len(preorder) - 1, self.curr)


x = Solution().buildTree(preorder = [1,2,3], inorder = [2,3,1])
print(x)

