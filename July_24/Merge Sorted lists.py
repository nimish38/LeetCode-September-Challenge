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

    def mergeTwoLists(self, list1, list2):
        list1 = self.build_LL(list1)
        list2 = self.build_LL(list2)
        if not list1 and not list2:
            return None
        first, head, res, node = True, None, None, None
        while list1 and list2:
            if list1.val <= list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next

            if first:
                res = head = node
                first = False
            else:
                res.next = node
                res = node

        while list1:
            if first:
                res = head = list1
                first = False
            else:
                res.next = list1
                res = list1
            list1 = list1.next

        while list2:
            if first:
                res = head = list2
                first = False
            else:
                res.next = list2
                res = list2
            list2 = list2.next

        return head


print(Solution().mergeTwoLists(list1 = [], list2 = [0]))