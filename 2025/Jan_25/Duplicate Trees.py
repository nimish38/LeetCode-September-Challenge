# Definition for a binary tree node.
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        nodes, res = defaultdict(int), []

        def solve(node):
            if not node:
                return 'N'
            curr = str(node.val) + ',' + solve(node.left) + ',' + solve(node.right)
            if nodes[curr] == 1:
                res.append(node)
            nodes[curr] += 1
            return curr
        solve(root)
        return res


l, m, n , o , c , d, e = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(2),TreeNode(4),TreeNode(4)
l.left, l.right = m , n
m.left, n. left, n.right = o, c, d
c.left = e
x = Solution().findDuplicateSubtrees(l)
print(x)