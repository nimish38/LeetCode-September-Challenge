class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or head.next:
            return head
        mid = splitlist(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        mergelist(left, right)

        return head