# Definition for singly-linked list.
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
    def oddEvenList(self, head):
        odd, even = head, head.next
        first, second = even.next, even.next.next

        while first:
            odd.next = first
            even.next = second
            first.next = even

            if second:
                odd = first
                even = second
                first = second.next
                second = first.next

        return head

Llist = LinkedList()
for i in range(1, 6):
    Llist.inserAtEnd(i)
head = Llist.returnHead()
Solution().oddEvenList(head)