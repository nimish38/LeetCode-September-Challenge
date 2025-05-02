class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second, slow.next = slow.next, None

        ahead, prev = second.next, None
        while second:
            ahead, second.next = second.next, prev
            second, prev = ahead, second

        i, j = head, prev
        while i and j:
            i_next, j_next = i.next, j.next
            i.next = j
            i = i_next
            j.next = i
            j = j_next
        return head


a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, c.next, d.next = b, c, d, e
x = Solution().reorderList(a)
print(x)
