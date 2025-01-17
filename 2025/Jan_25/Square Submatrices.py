class Solution:
    def countSquares(self, matrix):
        m, n, ones = len(matrix), len(matrix[0]), []
        sides, cnt = min(m, n), 0

        def checkSquare(a, b, val):
            for x in range(val):
                for y in range(val):
                    if not matrix[a + x][b + y]:
                        return False
            return True

        for side in range(sides, 0, -1):
            for i in range(0, m - side + 1):
                for j in range(0, n - side + 1):
                    if checkSquare(i, j, side):
                        cnt += 1
        return cnt


print(Solution().countSquares(matrix = [
    [1,1,0,0,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [0,0,1,0,1]]
))
