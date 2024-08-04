from collections import deque
class Solution:
    def levelOrder(self, root):
        qu, res = deque([root]), []
        while qu:
            lvl, num = [], len(qu)
            for _ in range(num):
                node = qu.popleft()
                lvl.append(node)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)

            res.append(lvl)
        return res
