class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def similar(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if (p and q) and p.val != q.val:
            return False
        return self.similar(p.left, q.left) and self.similar(p.right, q.right)

    def isSameTree(self, p, q) -> bool:
        return self.similar(p, q)


x, y = TreeNode(2), TreeNode(3)
z = TreeNode(1, x, y)

a, b = TreeNode(2), TreeNode(3)
c = TreeNode(1, a, b)

print(Solution().isSameTree(z, c))