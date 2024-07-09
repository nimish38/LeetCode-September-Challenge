# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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

    def deleteDuplicates(self, head):
        head = self.build_LL(head)
        curr = head
        while curr.next and curr.val == curr.next.val:
            curr = curr.next
        head = curr.next




        return head.val

print(Solution().deleteDuplicates(head = [1,1,2,3,3,4,4,5]))
