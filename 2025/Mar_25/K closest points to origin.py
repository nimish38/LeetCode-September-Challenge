class Solution:
    def kClosest(self, points, k: int):
        points.sort(key = lambda k: k[0]**2 + k[1]**2)
        return points[:k]


print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))