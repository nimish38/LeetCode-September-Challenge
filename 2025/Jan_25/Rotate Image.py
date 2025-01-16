class Solution:
    def rotate(self, matrix) -> None:
        n, temp = len(matrix), []
        for i in range(n):
            val = []
            for j in range(n - 1, -1, -1):
                val.append(matrix[j][i])
            temp.append(val)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]

        return matrix

