class Solution:
    def findMinArrowShots(self, points):
        points.sort()
        res, start, end = 0, points[0][0], points[0][1]
        for pt in points:
            if start <= pt[0] <= end or start <= pt[1] <= end:
                start, end = max(start, pt[0]), min(pt[1], end)
            else:
                res, start, end = res + 1, pt[0], pt[1]
        return res + 1

print(Solution().findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))