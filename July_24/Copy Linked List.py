class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None
        links1, links2, i = {}, {}, 0
        while head:
            links1[head] = i
            new_node = Node(head.val)
            links2[i] = new_node
            head = head.next
            i += 1

        for ele in links1:
            # print(ele.val, '-> ', links1[ele])
            if ele.next:
                index, target_index = links1[ele], links1[ele.next]
                links2[index].next = links2[target_index]
            if ele.random:
                index, target_index = links1[ele], links1[ele.random]
                links2[index].random = links2[target_index]
            else:
                links2[links1[ele]].random = None

        # for i in links2:
        #     print(links2[i].val ,'->', links2[i].next.val)
        return links2[0]


print(Solution().copyRandomList([[7,None],[13,0],[11,4],[10,2],[1,0]]))

