class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        n, cnt = len(rectangles), 0
        for i in range(n):
            rectangles[i] = rectangles[i][0] / rectangles[i][1]

        for i in range(n):
            for j in range(i + 1, n):
                if rectangles[j] == rectangles[i]:
                    cnt += 1
        return cnt

print(Solution().interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]]))
