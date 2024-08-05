from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        qu, res, l2r = deque([root]), [], True
        while qu:
            lvl, num = [], len(qu)
            for _ in range(num):
                if l2r:
                    node = qu.popleft()
                    if node.left:
                        qu.append(node.left)
                    if node.right:
                        qu.append(node.right)
                else:
                    node = qu.pop()
                    if node.right:
                        qu.append(node.right)
                    if node.left:
                        qu.append(node.left)
                lvl.append(node.val)
            l2r = not l2r
            res.append(lvl)
        return res

a, b, c = TreeNode(3), TreeNode(9), TreeNode(20)
a.left, a.right = b, c
c.left, c.right = TreeNode(15), TreeNode(7)
print(Solution().levelOrder(a))