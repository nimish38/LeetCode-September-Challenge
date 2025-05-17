class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        curr = root.val
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root