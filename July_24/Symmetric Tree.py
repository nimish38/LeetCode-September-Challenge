class Solution:
    def checkSymmetry(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left)

    def isSymmetric(self, root) -> bool:
        if not root.left and not root.right:
            return True
        return self.checkSymmetry(root.left, root.right)