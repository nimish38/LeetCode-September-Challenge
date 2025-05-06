class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        print(matrix)
print(Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))