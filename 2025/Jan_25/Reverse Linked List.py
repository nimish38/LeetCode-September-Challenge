# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        first, second = head, head.next
        while second:
            third = second.next
            second.next = first
            first, second = second, third
        head.next = None
        return first

    def buildList(self, nums):
        dummy = curr = ListNode('#')
        for num in nums:
            node = ListNode(num)
            curr.next = node
            curr = node
        return dummy.next


x = Solution().buildList([1,2,3,4,5])
y = Solution().reverseList(head = x)
print(y)