class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def build_LL(self, head, pos):
        first, prev = None, None
        for i in range(len(head)):
            a = ListNode(head[i])
            if i == 0:
                first = prev = a
            else:
                prev.next = a
                prev = a

        if pos != -1:
            i, cn = 0, first
            while cn:
                if i == pos:
                    prev.next = cn
                    break
                cn = cn.next
                i += 1
        return first


    def hasCycle(self, head, pos) -> bool:
        head = self.build_LL(head, pos)
        if not head:
            return False

        slow, fast = head, head.next
        while slow and fast and slow != fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
                break
        if slow and fast:
            return True
        return False


print(Solution().hasCycle(head = [3,2], pos = -1))