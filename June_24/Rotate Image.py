class Solution:
    def rotate(self, matrix):
        temp, n = [], len(matrix)
        for j in range(n):
            x = []
            for i in range(n - 1, -1, -1):
                x.append(matrix[i][j])
            temp.append(x)

        matrix = temp
        print(matrix)

Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

