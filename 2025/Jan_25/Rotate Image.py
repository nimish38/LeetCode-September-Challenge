class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j] = matrix[j][i]
        return matrix


print(Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))