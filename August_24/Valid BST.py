class Solution:
    def isValidBST(self, root) -> bool:
        left, right = True, True
        if root.left:
            if root.left.val >= root.val :
                return False
            left = self.isValidBST(root.left)

        if root.right:
            if root.right.val <= root.val :
                return False
            right = self.isValidBST(root.left)

        return left and right
