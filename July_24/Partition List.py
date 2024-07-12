class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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

    def partition(self, head, x: int):
        if not head:
            return head
        head = self.build_LL(head)
        before = ListNode(0)
        after = ListNode(0)
        beforeptr = before
        afterptr = after
        while(head):
            if (head.val<x):
                beforeptr.next = head
                beforeptr = head
            else:
                afterptr.next = head
                afterptr = head
            head=head.next
        afterptr.next =None
        beforeptr.next = after.next
        return before.next

print(Solution().partition(head = [1,4,3,0,2,5,2], x = 3))
