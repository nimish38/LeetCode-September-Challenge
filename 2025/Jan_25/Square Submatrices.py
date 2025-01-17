class Solution:
    def countSquares(self, matrix):
        m, n, ones = len(matrix), len(matrix[0]), []
        sides, cnt = min(m, n), 0

        def row(a, b, val):
            for _ in range(val):
                if not matrix[a][b + _]:
                    return False
            return True

        def col(a, b, val):
            for _ in range(val):
                if not matrix[a + _][b]:
                    return False
            return True

        def diag(a, b, val):
            for _ in range(val):
                if not matrix[a + _][b + _]:
                    return False
            return True

        for side in range(sides, 0, -1):
            for i in range(0, m - side + 1):
                for j in range(0, n - side + 1):
                    if row(i, j, side) and col(i, j, side) and diag(i, j, side):
                        cnt += 1


        return cnt


print(Solution().countSquares(matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
