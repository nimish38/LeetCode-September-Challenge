from collections import deque
import math

class Solution(object):
    def numSquares(self, n):
        val, avail = int(math.sqrt(n)), []
        for i in range(val, 0, -1):
            avail.append(i ** 2)
        que, next_que, cnt = {n}, set(),  0
        while que:
            for node in que:
                if node == 0:
                    return cnt
                for num in avail:
                    if node - num >= 0:
                        next_que.add(node - num)
            cnt += 1
            que, next_que = next_que, set()
        return cnt

print(Solution().numSquares(12))