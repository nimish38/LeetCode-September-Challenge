class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1:
            return head

        def reverse(node):
            c = node
            for _ in range(k):
                if not c:
                    return (node, False)
                c = c.next
            a, b = node, node.next,
            for _ in range(k - 1):
                temp = b.next
                b.next = a
                a, b = b, temp
            node.next = c
            if c:
                return (a, True)
            return (a, False)

        dummy = ListNode(-1, head)
        prev, remain = dummy, True
        while remain:
            curr = prev.next
            new_head, remain = reverse(prev.next)
            prev.next = new_head
            prev = curr
        return dummy.next

# a ,b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
# a.next, b.next, c.next, d.next = b, c, d, e
a ,b = ListNode(1), ListNode(2)
a.next = b
x = Solution().reverseKGroup(a, 2)
print(x)