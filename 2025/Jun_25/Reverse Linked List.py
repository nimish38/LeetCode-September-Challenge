class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        a, b, c = head, head.next, head.next.next
        while b:
            b.next = a
            a, b = b, c
            if c:
                c = c.next
        head.next = None
        return a

a ,b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, c.next, d.next = b, c, d, e
x = Solution().reverseList(a)
print(x.val)