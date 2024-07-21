class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        def construct(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return
            root, i = TreeNode(postorder[post_end]), in_start
            while i <= in_end and inorder[i] != root.val:
                i += 1
            left_subarray, right_subarray = i - in_start, in_end - i
            if right_subarray:
                root.right = construct(i + 1, in_end, post_end - right_subarray, post_end - 1)
            if left_subarray:
                root.left = construct(in_start, i - 1, post_start, post_start + left_subarray - 1)
            return root

        n = len(inorder) - 1
        return construct(0, n, 0, n)

x = Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(x.val)