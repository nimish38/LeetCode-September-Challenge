from collections import deque
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
