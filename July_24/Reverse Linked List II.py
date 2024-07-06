class Solution:
    def reverseBetween(self, head, left: int, right: int):
        curr, i, vals = head, 1, []
        while curr:
            if left <= i <= right:
                vals.append(curr.val)
            curr = curr.next
            i += 1
        curr, i = head, 1
        while curr:
            if left <= i <= right:
                curr.val = vals.pop()
            curr = curr.next
            i += 1
        return head

print(Solution().reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))
