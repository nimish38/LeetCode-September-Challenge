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
        return mat

print(Solution().spiralMatrix(3, 5, None))
