class Solution:
    def spiralOrder(self, matrix):
        res = []
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while up >= down and left >= right:
            # Right
            for i in range(left, right):
                res.append(matrix[up][i])
            up += 1

            # Down
            for i in range(up, down):
                res.append(matrix[right][i])
            right -= 1

            # Left
            for i in range(right, left - 1, -1):
                res.append(matrix[i][down])
            down -= 1

            # Up
            for i in range(down, up - 1, -1):
                res.append(matrix[left][i])
            left += 1