from collections import deque
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

    