class Solution:
    def reverseList(self, head):
        if not head or head.next:
            return head
        p, c, n = head, head.next, None
        while c:
            n, c.next = c.next, p
            p, c = c, n
        return p
    