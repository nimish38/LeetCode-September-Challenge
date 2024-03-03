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
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        maxsum, n = -1, len(nums)
        for i in range(n//2):
            if nums[i] + nums[n - 1 - i] > maxsum:
                maxsum = nums[i] + nums[n - 1 -i]
        return maxsum

Llist = LinkedList()
for i in [2,11,3,5,6,8]:
    Llist.inserAtEnd(i)
head = Llist.returnHead()
print(Solution().TwinSumLinkedList(head))
