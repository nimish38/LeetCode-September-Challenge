class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def reverseKGroup(self, head, k: int):
        head = self.build_LL(head)
        new_head = self.rever_LL(head)
        # dummy = ListNode(-1)
        # dummy.next = head

print(Solution().reverseKGroup(head = [1,2,3,4,5], k = 2))