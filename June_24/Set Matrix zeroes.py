class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for r in range(m):
            if matrix[r][0] == 0:
                matrix[r] = [0] * n

        for c in range(n):
            if matrix[0][c] == 0:
                for i in range(1, m):
                    matrix[i][c] = 0

        print(matrix)

Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
