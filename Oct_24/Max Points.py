class Solution:
    def maxPoints(self, points) -> int:
        res, n = 0, len(points)
        if n == 1:
            return 1
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 2
                x1, y1 = points[i][0], points[i][1]
                if points[j][0] != x1:
                    slope = (points[j][1] - y1) / (points[j][0] - x1)
                else:
                    slope = float('inf')
                for k in range(n):
                    if k != i and k != j:
                        if points[k][0] != x1:
                            new_slope = (points[k][1] - y1) / (points[k][0] - x1)
                        else:
                            new_slope = float('inf')
                        if slope == new_slope:
                            cnt += 1

                res = max(res, cnt)
        return res

print(Solution().maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
