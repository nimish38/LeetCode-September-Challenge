class Solution:
    def transpose(self, matrix):
        res = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[i][j])
            res.append(row)
        return res

    