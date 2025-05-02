class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and slow != fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
        return slow == fast

a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(4)
a.next, b.next, c.next, d.next = b, c, d, b
print(Solution().hasCycle(a))