class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root, lsub = [], rsub = []) -> bool:
        left, right = True, True
        if root.left:
            rsub.append(root.val)
            for value in rsub:
                if root.left.val >= value :
                    return False
            left = self.isValidBST(root.left, lsub, rsub)

        if root.right:
            lsub.append(root.val)
            for value in lsub:
                if root.right.val <= value :
                    return False
            right = self.isValidBST(root.right, lsub, rsub)

        return left and right

# a, b, c = TreeNode(5), TreeNode(4), TreeNode(1)
# a.right, a.left = b, c
# b.left, b.right = TreeNode(3), TreeNode(2)

a, b = TreeNode(0), TreeNode(1)
a.right = b
print(Solution().isValidBST(a))