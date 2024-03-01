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
        if not head: return None
        odd = oddHead = head
        evenHead = even = head.next

        while odd.next and even.next:
            # Connect the current odd node to the next odd node
            odd.next = odd.next.next
            # Move the current odd node to the next odd node
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return oddHead

Llist = LinkedList()
for i in [2,1,3,5,6,4,7]:
    Llist.inserAtEnd(i)
head = Llist.returnHead()
Solution().oddEvenList(head)
print(head)