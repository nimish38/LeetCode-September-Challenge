from collections import deque


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res, que = [], deque([root])
        while que:
            cnt, lvl = len(que), []
            for _ in range(cnt):
                node = que.popleft()
                lvl.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(lvl)
        return res
