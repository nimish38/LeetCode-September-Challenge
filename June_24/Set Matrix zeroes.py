class Solution:
    def setZeroes(self, matrix):
        row, col, n = set(), set(), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for r in row:
            matrix[r] = [0] * n

        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0

        print(matrix)

Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
