class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        rowStart, colStart, rowEnd, colEnd = -1, 0, -1, 0

        for i in range(n):
            if colStart == -1 and matrix[0][i] <= target <= matrix[m - 1][i]:
                colStart, colEnd = i, i
            elif colStart != -1 and matrix[0][i] <= target <= matrix[m - 1][i]:
                colEnd = i

        for i in range(m):
            if rowStart == -1 and matrix[i][colStart] <= target <= matrix[i][colEnd]:
                rowStart, rowEnd = i, i
            elif rowStart != -1 and  matrix[i][colStart] <= target <= matrix[i][colEnd]:
                rowEnd = i

        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                if matrix[i][j] == target:
                    return True
        return False



