class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        for i in range(1, left):
            prev = prev.next

        start = first = prev.next
        if first:
            curr = first.next
        if curr:
            second = curr.next

        for i in range(left, right):
            curr.next = first
            first, curr, second = curr, second, second.next

        prev.next = curr
        start.next = second
        return dummy.next

print(Solution().reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))
