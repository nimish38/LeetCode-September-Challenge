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

    def reverse_LL(self, node):
        prev = node
        curr, succ = prev.next, prev.next.next
        node.next = None
        while curr:
            curr.next = prev
            prev, curr = curr, succ
            if succ:
                succ = succ.next
        return prev

    def reverseKGroup(self, head, k: int):
        head = self.build_LL(head)
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, lastFlag,  = dummy, False
        next_node = prev.next
        while not lastFlag:
            curr, temp = next_node, next_node
            for i in range(k - 1):
                if not temp:
                    lastFlag = True
                    break
                temp = temp.next
            if not temp or lastFlag:
                prev.next = curr
                lastFlag = True
            else:
                next_node = temp.next
                temp.next = None
                self.reverse_LL(curr)
                prev.next = temp
                prev = curr

        return dummy.next



print(Solution().reverseKGroup(head = [1,2], k = 2))