class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return None
        links1, links2, i, prev = {}, {}, 0, None
        while head:
            links1[head] = i
            new_node = Node(head.val)
            links2[i] = new_node
            head = head.next
            i += 1
            if prev:
                prev.next = new_node
            else:
                prev = new_node

        for ele in links1:
            if ele.random:
                index, target_index = links1[ele], links1[ele.random]
                links2[index].random = links2[target_index]
            else:
                links2[links1[ele]].random = None

        return links2[0]


print(Solution().copyRandomList([[7,None],[13,0],[11,4],[10,2],[1,0]]))

