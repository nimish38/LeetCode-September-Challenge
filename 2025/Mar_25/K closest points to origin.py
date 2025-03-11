class Solution:
    def kClosest(self, points, k: int):
        dis = []
        for x, y in points:
            val = (x ** 2) + (y ** 2)
            dis.append([val, [x, y]])

        dis.sort(key=lambda x: x[0])
        return dis[:k]


print(Solution)