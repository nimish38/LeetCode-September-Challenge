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

    def partition(self, head, x: int):
        if not head:
            return head
        head = self.build_LL(head)
        dummy = ListNode(-420, head)

        insertPos = curr = dummy
        largeFound = False
        while curr.next:
            if curr.next.val < x and largeFound:
                temp, succ = curr.next, curr.next.next
                curr.next = succ
                partition = insertPos.next
                partition.next = temp
                temp.next = partition
            else:
                largeFound = True
            curr = curr.next

        return dummy.next

print(Solution().partition(head = [1,4,3,2,5,2], x = 3))
