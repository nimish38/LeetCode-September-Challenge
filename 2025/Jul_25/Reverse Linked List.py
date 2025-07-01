# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev, curr = head, head.next
        while curr:
            succ = curr.next
            curr.next = prev
            prev, curr = curr, succ
        head.next = None
        return prev