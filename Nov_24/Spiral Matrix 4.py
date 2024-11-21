# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        mat = []
        for i in range(m):
            x = []
            for j in range(n):
                x.append((i, j))
            mat.append(x)

        up, down, left, right = 0, m - 1, 0, n - 1
        while up <= down and left <= right:

            for i in range(left, right + 1):
                print(mat[up][i])
            up += 1

            for i in range(up, down + 1):
                print(mat[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                print(mat[down][i])
            down -= 1

            for i in range(down, up - 1, -1):
                print(mat[i][left])
            left += 1

print(Solution().spiralMatrix(4, 3, None))
