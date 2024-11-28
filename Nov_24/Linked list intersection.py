class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        l1, l2,curr = 0, 0, headA
        while curr:
            l1 += 1
            curr = curr.next

        curr = headB
        while curr:
            l2 += 1
            curr = curr.next

        t1, t2 = headA, headB
        if l1 > l2:
            while l1 > l2:
                t1 = t1.next
                l1 -= 1

        if l2 > l1:
            while l2 > l1:
                t2 = t2.next
                l2 -= 1

        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
        return t1


a, b, c, d, e = ListNode(4),ListNode(1),ListNode(8),ListNode(4),ListNode(5),
p, q, r = ListNode(5),ListNode(6),ListNode(1)

a.next, b.next, c.next, d.next, p.next, q.next, r.next = b, c, d, e, q, r, c
x = Solution().getIntersectionNode(a, p)
print(x.val)