class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val <= l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        start, end = 0, len(lists) - 1
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])

        return merge(list1, list2)


a, b, c = ListNode(1), ListNode(4), ListNode(5)
a.next, b.next = b, c
p, q, r = ListNode(1), ListNode(3), ListNode(4)
p.next, q.next = q, r
x, y = ListNode(2), ListNode(6)
x.next = y
z = Solution().mergeKLists([a, p, x])
print(z)