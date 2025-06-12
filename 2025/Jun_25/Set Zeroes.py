class Solution(object):
    def setZeroes(self, matrix):
        m, n, firstRow, firstCol = len(matrix), len(matrix[0]), False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRow:
            matrix[0] = [0] * n
        if firstCol:
            for _ in range(m):
                matrix[_][0] = 0
        return matrix

print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))