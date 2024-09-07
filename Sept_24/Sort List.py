class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):

        def splitlist(node):
            slow, fast = node, node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            return right

        if not head or head.next:
            return head
        mid = splitlist(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        mergelist(left, right)

        return head