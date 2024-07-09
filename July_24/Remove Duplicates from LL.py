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
        if not head or not head.next:
            return head
        dummy = ListNode(-420, head)
        lastUnique, curr, prev = dummy, head.next, head
        while curr:
            if not prev:
                prev = curr
            else:
                if prev.val == curr.val:
                    lastUnique.next = curr.next
                    prev = None
                else:
                    lastUnique = prev
                    prev = curr
            curr = curr.next
        return dummy.next

print(Solution().deleteDuplicates(head = [1,1,2,3,3,4,4,5]))
