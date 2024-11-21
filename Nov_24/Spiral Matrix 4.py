# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        mat = []
        for i in range(m):
            mat.append([-1] * n)

        up, down, left, right = 0, m - 1, 0, n - 1
        while up <= down and left <= right and head:

            for i in range(left, right + 1):
                if head:
                    mat[up][i] = head.val
                    head = head.next
            up += 1

            for i in range(up, down + 1):
                if head:
                    mat[i][right] = head.val
                    head = head.next
            right -= 1

            for i in range(right, left - 1, -1):
                if head:
                    mat[down][i] = head.val
                    head = head.next
            down -= 1

            for i in range(down, up - 1, -1):
                if head:
                    mat[i][left] = head.val
                    head = head.next
            left += 1

        return mat


val, head = [3,0,2,6,8,1,7,9,4,2,5,5,0], ListNode(-1)
dummy = head
for v in val:
    dummy.next = ListNode(v)
    dummy = dummy.next

print(Solution().spiralMatrix(3, 5, head.next))
