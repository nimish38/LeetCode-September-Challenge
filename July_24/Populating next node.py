class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = [root]
        while level:
            nodes = len(level)
            for i in range(nodes):
                poped = level.pop()
                if i < nodes - 1:
                    poped.next = level[0]
                if poped.left:
                    level.append(poped.left)
                if poped.right:
                    level.append(poped.right)
        return root
