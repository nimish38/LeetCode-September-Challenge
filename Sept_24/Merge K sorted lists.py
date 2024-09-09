class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        vals = []
        for list in lists:
            curr = list
            while curr:
                vals.append(curr.val)
                curr = curr.next
        vals.sort()
        curr = dummy = ListNode('$')

        for num in vals:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next