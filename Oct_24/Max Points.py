from collections import defaultdict
class Solution:
    def maxPoints(self, points) -> int:
        res, n = 0, len(points)
        if n == 1:
            return 1
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    dx, dy = points[j][1] - points[i][1], points[j][0] - points[i][0]
                    if dx == 0:
                        cnt['*'] += 1
                    else:
                        cnt[dy/dx] += 1
            val = 0
            for i in cnt:
                val = max(val, cnt[i])
            res = max(res, val)

        return res

print(Solution().maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
