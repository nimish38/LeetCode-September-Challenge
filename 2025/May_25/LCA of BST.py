class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p.val, q.val)
        return root