class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def reverseBetween(self, head, left: int, right: int):
        head = self.build_LL(head)
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        for i in range(1, left):
            prev = prev.next

        start = first = prev.next
        curr = second = None
        if first:
            curr = first.next
        if curr:
            second = curr.next

        for i in range(left, right):
            curr.next = first
            first, curr, second = curr, second, second.next
            if second:
                second = second.next
        prev.next = first
        start.next = curr
        return dummy.next

print(Solution().reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))
