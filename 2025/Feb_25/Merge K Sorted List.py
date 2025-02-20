# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return []
        elif k == 1:
            return lists[0]
        else:
            l = merge(lists[0], lists[1])
            for i in range(2, k):
                l = merge(l, lists[i])
            return l
        