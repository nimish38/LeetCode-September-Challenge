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
        left, cnt = head, 0
        while left:
            cnt += 1
            left = left.next

        k %= cnt
        right = left = head
        for _ in range(k):
            right = right.next

        
