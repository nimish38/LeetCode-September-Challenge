class NumMatrix(object):

    def __init__(self, matrix):
        n, self.mat = len(matrix), matrix
        for i in range(n):
            for j in range(1, n):
                self.mat[i][j] += self.mat[i][j - 1]

        for j in range(n):
            for i in range(1, n):
                self.mat[i][j] += self.mat[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        upperRight, upperLeft, bottomLeft = 0, 0, 0
        if row1 > 0:
            upperRight = self.mat[row1][col2]
        if col1 > 0:
            if row1 > 0:
                upperLeft = self.mat[row1 - 1][col1 - 1]
            bottomLeft = self.mat[row2][col1 - 1]
        return (self.mat[row2][col2] - upperRight) - (bottomLeft - upperLeft)

