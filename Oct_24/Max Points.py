class Solution:
    def maxPoints(self, points) -> int:
        res, n = 0, len(points)
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 2
                x1, y1 = points[i][0], points[i][1]
                slope = (points[j][1] - y1) / (points[j][0] - x1)

            for k in range(n):
                if k != i and k != j:
                    new_slope = (points[k][1] - y1) / (points[k][0] - x1)
                    if slope == new_slope:
                        cnt += 1

            res = max(res, cnt)
        return res
