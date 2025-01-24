class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        i, j, n, best = 0, 1, len(points), float('-inf')
        while i < n - 1:
            j = i + 1
            while j < n and (points[j][0] - points[i][0]) <= k:
                best = max(best, points[i][1] + points[j][1] + (points[j][0] - points[i][0]))
                j += 1
            i += 1
        return best


print(Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))