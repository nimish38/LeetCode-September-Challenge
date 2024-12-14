class Solution:
    def transpose(self, matrix):
        res = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            res.append(row)
        return res

print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))