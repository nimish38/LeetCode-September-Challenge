class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None
        t1, t2 = headA, headB
        while t1 != t2:
            t1, t2 = t1.next, t2.next
            if t1 == t2:
                return t1
            if not t1:
                t1 = headB
            if not t2:
                t2 = headA
        return t1


a, b, c, d, e = ListNode(4),ListNode(1),ListNode(8),ListNode(4),ListNode(5),
p, q, r = ListNode(5),ListNode(6),ListNode(1)

a.next, b.next, c.next, d.next, p.next, q.next, r.next = b, c, d, e, q, r, c
x = Solution().getIntersectionNode(a, p)
print(x.val)