class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None
        new_head, prev, curr, corresponding = None, None, head, {}
        while curr:
            new_node = Node(curr.val)
            if new_head is None:
                new_head = new_node
            else:
                prev.next = new_node
            corresponding[curr] = new_node
            prev = new_node
            curr = curr.next

        curr, new_curr = head, new_head
        while curr:
            if curr.random:
                new_curr.random = corresponding[curr.random]
            curr = curr.next
            new_curr = new_curr.next
        return new_head


print(Solution().copyRandomList([[7,None],[13,0],[11,4],[10,2],[1,0]]))

