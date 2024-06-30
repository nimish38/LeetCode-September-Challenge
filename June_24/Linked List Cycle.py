class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False

        slow, fast = head, head.next
        while slow and fast and slow != fast:
            slow = slow.next
            if slow:
                fast = slow.next

        return slow == fast


print(Solution().hasCycle())