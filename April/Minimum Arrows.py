class Solution:
    def findMinArrowShots(self, points):
        if len(points) < 2:
            return 1
        points.sort(key=lambda x: x[1])
        cnt = 0
        last_arrow = points[0][1]
        for j in range(1, len(points)):
            if points[j][0] > last_arrow:
                cnt += 1
                last_arrow = points[j][1]
        return cnt + 1

print(Solution().findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))


