class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        new_head = curr = ListNode(-101)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return new_head.next

    def mergeKLists(self, lists):

        def partition(s, e):
            if s == e:
                return lists[s]
            mid = (s + e) // 2
            left, right = partition(s, mid), partition(mid + 1, e)
            return self.mergeTwoLists(left, right)

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return partition(0, len(lists) - 1)