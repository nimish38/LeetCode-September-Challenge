class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(-1)
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val
            if carry:
                val += 1
                carry = 0
            newnode = ListNode(val % 10)
            carry = val // 10
            curr.next, curr = newnode, newnode
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            if carry:
                val += 1
                carry = 0
            newnode = ListNode(val % 10)
            carry = val // 10
            curr.next, curr = newnode, newnode
            l1 = l1.next

        while l2:
            val = l2.val
            if carry:
                val += 1
                carry = 0
            newnode = ListNode(val % 10)
            carry = val // 10
            curr.next, curr = newnode, newnode
            l2 = l2.next

        if carry:
            curr.next = ListNode(1)

        return dummy.next