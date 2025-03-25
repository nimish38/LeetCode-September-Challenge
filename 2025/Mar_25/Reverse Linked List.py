class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p, c, n = head, head.next, None
        p.next = None
        while c:
            n, c.next = c.next, p
            p, c = c, n
        return p


a, b, c, d, e = Node(1), Node(2), Node(3), Node(4), Node(5)
a.next, b.next, c.next, d.next = b, c, d, e
x = Solution().reverseList(a)
print(x)
