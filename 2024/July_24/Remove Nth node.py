class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def build_LL(self, head):
        first, prev = None, None
        for i in range(len(head)):
            a = ListNode(head[i])
            if i == 0:
                first = prev = a
            else:
                prev.next = a
                prev = a
        return first

    def removeNthFromEnd(self, head, n: int):
        head = self.build_LL(head)
        dummy = ListNode(-1, head)

        left = right = dummy
        for _ in range(n + 1):
            right = right.next

        # when light reaches end of list, left is at correct position

        while(right):
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


print(Solution().removeNthFromEnd(head = [2,1], n = 1))
