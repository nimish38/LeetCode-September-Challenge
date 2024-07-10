class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def build_LL(self, head):
        first, prev = None, None
        for i in range(len(head)):
            a = ListNode(head[i])
            if i == 0:
                first = prev = a
            else:
                prev.next = a
                prev = a
        return first

    def rotateRight(self, head, k: int):
        head = self.build_LL(head)
        if not head or not head.next or k is 0:
            return head
        left, cnt = head, 0
        while left:
            cnt += 1
            left = left.next
        if k == cnt:
            return head
        k %= cnt
        right = left = head
        for _ in range(k):
            right = right.next

        while right.next:
            right = right.next
            left = left.next
        temp = left.next
        left.next = None
        right.next = head
        return temp

print(Solution().rotateRight(head = [0,1,2], k = 4))