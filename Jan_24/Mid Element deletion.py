# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        fast, slow, prev = head, head, head
        if head.next:
            while fast.next and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if fast.next:
                prev = slow
                slow = slow.next

            prev.next = slow.next
            slow.next = None
            del slow
            return head
        return None