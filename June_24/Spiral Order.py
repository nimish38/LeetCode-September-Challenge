class Solution:
    def spiralOrder(self, matrix):
        res, n = [], len(matrix) * len(matrix[0])
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while len(res) < n:
            # Right
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if len(res) == n:
                break

            # Down
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if len(res) == n:
                break

            # Left
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if len(res) == n:
                break

            # Up
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if len(res) == n:
                break

        return res

print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))