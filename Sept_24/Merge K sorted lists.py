class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        start, end = 0, len(lists) - 1
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])

        return merge(list1, list2)