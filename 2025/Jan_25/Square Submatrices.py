class Solution:
    def countSquares(self, matrix):
        m, n, ones = len(matrix), len(matrix[0]), []
        sides, cnt = min(m, n), 0

        for side in range(sides, 0, -1):
            for i in range(0, m - side):
                for j in range(0, n - side):
                    if row(i, j, side) and col(i, j, side) and diag(i, j, side):
                        cnt += 1

        return cnt
