class Solution:
    def spiralOrder(self, matrix):
        res, m, n = [], len(matrix), len(matrix[0])
        left, right, top, down = 0, n - 1, 0, m - 1

        while left <= right and top <= down:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right or top > down:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1

            for i in range(down, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

print(Solution().spiralOrder(matrix = [[6,9,7]]))