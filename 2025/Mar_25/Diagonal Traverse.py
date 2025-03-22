class Solution:
    def findDiagonalOrder(self, mat):
        m, n, res, i, j = len(mat), len(mat[0]), [], 0, 0
        while not (i == m - 1 and j == n - 1):
            res.append(mat[i][j])

            while i - 1 >= 0 and j + 1 < n:
                i -= 1
                j += 1
                res.append(mat[i][j])

            if j + 1 < n:
                j += 1
            else:
                i += 1
            res.append(mat[i][j])

            while i + 1 < m and j - 1 >= 0:
                i += 1
                j -= 1
                res.append(mat[i][j])

            if i + 1 < m:
                i += 1
            else:
                j += 1

        res.append(mat[i][j])
        return res


print(Solution().findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))