# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def makeLists(self, lists):
        def build(val):
            dummy = curr = ListNode(-1)
            for v in val:
                curr.next = ListNode(v)
                curr = curr.next
            return dummy.next
        lis = []
        for a in lists:
            lis.append(build(a))
        return lis

    def mergeKLists(self, lists):
        def merge(l1, l2):
            dummy = curr = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next

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


a = Solution().makeLists(lists = [[1,4,5],[1,3,4],[2,6]])
x = Solution().mergeKLists(a)
print(x)