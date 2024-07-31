class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        l_depth, r_depth = 0, 0
        l, r = root, root
        while l:
            l_depth += 1
            l = l.left
        while r:
            r_depth += 1
            r = r.right

        if l_depth == r_depth:
            return 2 ** l_depth - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

m, n, o = TreeNode(4), TreeNode(5), TreeNode(6)
p, q = TreeNode(2), TreeNode(3)
p.left, p.right, q.left = m, n, o
r = TreeNode(1)
r.left, r.right = p, q
print(Solution().countNodes(r))