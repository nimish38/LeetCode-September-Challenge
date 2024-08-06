from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        left, right, res, l2r = [root], [], [], True
        while left or right:
            lvl = []
            if l2r:
                while left:
                    node = left.pop()
                    if node.left:
                        right.append(node.left)
                    if node.right:
                        right.append(node.right)
                    lvl.append(node)
            else:
                while right:
                    node = right.pop()
                    if node.right:
                        left.append(node.right)
                    if node.left:
                        left.append(node.left)
                    lvl.append(node)
            l2r = not l2r
            res.append(lvl)
        return res

a, b, c = TreeNode(3), TreeNode(9), TreeNode(20)
a.left, a.right = b, c
c.left, c.right = TreeNode(15), TreeNode(7)
print(Solution().zigzagLevelOrder(a))