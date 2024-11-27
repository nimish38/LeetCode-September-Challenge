class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodes, curr = {}, headA
        while curr:
            nodes[curr] = curr.val
            curr = curr.next

        curr = headB
        while curr:
            if curr in nodes:
                return curr
        return None


