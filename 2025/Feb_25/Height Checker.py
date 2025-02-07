class Solution:
    def heightChecker(self, heights) -> int:
        expected, cnt = heights.copy(), 0
        expected.sort()
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                cnt += 1
        return cnt


