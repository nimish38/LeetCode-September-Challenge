class Solution:
    def similar(self, p, q):
        if (not p and q) or (p and not q):
            return False
        if (p and q) and p.val != q.val:
            return False
        return self.similar(p.left, q.left) and self.similar(p.right, q.right)

    def isSameTree(self, p, q) -> bool:
        return self.similar(p, q)

