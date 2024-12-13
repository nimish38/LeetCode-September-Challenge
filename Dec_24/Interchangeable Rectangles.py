from collections import defaultdict
class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        n, ratios, cnt = len(rectangles), defaultdict(int), 0
        for i in range(n):
            val = rectangles[i][0] / rectangles[i][1]
            ratios[val] += 1
        for count in ratios:
            cnt += (ratios[count] * (ratios[count] - 1)) // 2
        return cnt



print(Solution().interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]]))
