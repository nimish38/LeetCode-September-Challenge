class Solution:
    def kClosest(self, points, k: int):
        dis, res = [], []
        for x, y in points:
            val = (x ** 2) + (y ** 2)
            dis.append([val, [x, y]])

        dis.sort(key=lambda x: x[0])

        for i in range(k):
            res.append(dis[i][1])
        return res
    

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))