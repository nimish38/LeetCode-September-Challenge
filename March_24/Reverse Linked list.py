class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def inserAtEnd(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def returnHead(self):
        return self.head


class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        prev, post = None, head.next

        while post:
            head.next = prev
            prev = head
            head = post
            post = post.next

        head.next = prev
        return head



Llist = LinkedList()
for i in [2,1,3,5,6]:
    Llist.inserAtEnd(i)
head = Llist.returnHead()
Solution().reverseList(head)
print(head)
