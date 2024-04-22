class Solution:
    def findMinArrowShots(self, points):
        if len(points) < 2:
            return 1
        points.sort()
        i, j, cnt = 0, 1, 0
        last_arrow = points[i][1]
        while j < len(points):
            if points[j][0] <= last_arrow:
                j += 1
            else:
                cnt += 1
                last_arrow = points[j][1]
                j += 1
        return cnt

print(Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))


