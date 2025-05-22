class Solution(object):
    def spiralOrder(self, matrix):
        up, down, left, right, res = 0, len(matrix) - 1, 0, len(matrix[0]) - 1, []
        while up <= down and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1

            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right or up > down:
                return res

            for i in range(right, left - 1, - 1):
                res.append(matrix[down][i])
            down -= 1

            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res