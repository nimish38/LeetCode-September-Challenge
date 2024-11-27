class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodes, curr = {}, headA
        while curr:
            nodes[curr] = curr.val
            curr = curr.next

        curr = headB
        while curr:
            if curr in nodes:
                return curr
            curr = curr.next
        return None


a, b, c, d, e = ListNode(4),ListNode(1),ListNode(8),ListNode(4),ListNode(5),
p, q, r = ListNode(5),ListNode(6),ListNode(1)

a.next, b.next, c.next, d.next, p.next, q.next, r.next = b, c, d, e, q, r, c
x = Solution().getIntersectionNode(a, p)
print(x.val)