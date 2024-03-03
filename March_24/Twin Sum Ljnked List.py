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
    def TwinSumLinkedList(self, head):
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        last = None

        while fast:
            temp = fast.next
            fast.next = last
            last = fast
            fast = temp

        maxsum = -1
        while head and last:
            if head.val + last.val > maxsum:
                maxsum = head.val + last.val
            head = head.next
            last = last.next
        return maxsum



Llist = LinkedList()
for i in [2,11,3,5,6,8]:
    Llist.inserAtEnd(i)
head = Llist.returnHead()
print(Solution().TwinSumLinkedList(head))
