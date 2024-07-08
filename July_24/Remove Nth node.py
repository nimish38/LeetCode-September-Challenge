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

    def removeNthFromEnd(self, head, n: int):
        head = self.build_LL(head)
        dummy = ListNode(-1)
        dummy.next = head

        i, curr = 0, head
        while curr:
            curr = curr.next
            i += 1
        return i

print(Solution().removeNthFromEnd(head = [1,2,3,4,5], n = 2))
