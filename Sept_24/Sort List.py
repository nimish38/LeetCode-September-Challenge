class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        curr, vals = head, []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        vals.sort()
        curr, i = head, 0
        while curr:
            curr.val = vals[i]
            curr = curr.next
            i += 1
        return head