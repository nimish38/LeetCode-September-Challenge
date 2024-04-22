class Solution:
    def findMinArrowShots(self, points):
        if len(points) < 2:
            return 1
        points.sort()
        j, cnt = 1, 0
        start, end = points[0][0], points[0][1]
        while j < len(points):
            if points[j][0] <= end:
                start = max(start, points[j][0])
                end = min(end, points[j][1])
                j += 1
            else:
                cnt += 1
                start, end = points[j][0], points[j][1]
                j += 1
        return cnt + 1

print(Solution().findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))


