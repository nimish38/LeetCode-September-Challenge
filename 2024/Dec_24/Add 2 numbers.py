class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        res = int(s1[::-1]) + int(s2[::-1])
        res = list(str(res)[::-1])
        return self.build(list(map(int, res)))

    def build(self, nums):
        root = curr = ListNode(nums[0])
        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            curr.next = node
            curr = node
        return root


a = Solution().build([2,4,3])
b = Solution().build([5,6,4])
c = Solution().addTwoNumbers(a, b)
print(c)