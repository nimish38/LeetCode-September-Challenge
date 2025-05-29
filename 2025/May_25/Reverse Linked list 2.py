class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or not head.next:
            return head

        def reverse(node, number):
            if not node or not node.next:
                return node
            one, two, three = node, node.next, node.next.next
            while number > 0:
                two.next = one
                one, two = two, three
                if three:
                    three = three.next
                number -= 1
            return one

        cnt, start, end, dummy = 0, None, None, ListNode('#', head)
        curr = start_prev = dummy
        while cnt < right:
            if cnt == left - 1:
                start_prev = curr
            curr = curr.next
            cnt += 1
        start, end_next = start_prev.next, curr.next
        new_start = reverse(start, right - left)
        start_prev.next = new_start
        start.next = end_next
        return dummy.next

a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
a.next, b.next, c.next = b, c, d
x = Solution().reverseBetween(a, 1, 4)
print(x)