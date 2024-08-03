from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        qu, res = deque([root]), []
        while qu:
            val, num = 0, len(qu)
            for _ in range(num):
                node = qu.popleft()
                val += node.val
            res.append(val / num)
        return res

a, b, c = TreeNode(3), TreeNode(9), TreeNode(20)
a.left, a.right = b, c
c.left, c.right = TreeNode(15), TreeNode(7)
print(Solution().averageOfLevels(a))