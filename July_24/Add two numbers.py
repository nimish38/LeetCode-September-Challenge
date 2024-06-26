class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

    def addTwoNumbers(self, l1, l2):
        l1 = self.build_LL(l1)
        l2 = self.build_LL(l2)
        res = head = ListNode(0)
        first, carry = True, 0
        while l1 or l2:
            num1 = num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            value = carry + num1 + num2
            carry = value // 10
            value %= 10
            if first:
                res.val = value
                first = False
            else:
                newNode = ListNode(value)
                res.next = newNode
                res = newNode
        if carry:
            newNode = ListNode(1)
            res.next = newNode
        return head

print(Solution().addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))
