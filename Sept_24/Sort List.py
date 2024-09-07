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

        def mergelist(l, r):
            tail = dummy = ListNode('$')
            while l and r:
                if l.val < r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next
            if l:
                tail.next = l
            if r:
                tail.next = r
            return dummy.next

        if not head or head.next:
            return head
        mid = splitlist(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        mergelist(left, right)

        return head