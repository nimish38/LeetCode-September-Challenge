class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        n = len(rectangles)
        for i in range(n):
            rectangles[i] = rectangles[i][0] / rectangles[i][1]
        print(rectangles)

Solution().interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]])
