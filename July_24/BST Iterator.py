class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.curr, self.st = root, []
        while self.curr:
            self.st.append(self.curr)
            self.curr = self.curr.left

    def next(self) -> int:
        node = self.st.pop()
        self.curr = node.right
        while self.curr:
            self.st.append(self.curr)
            self.curr = self.curr.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.st) >= 1


a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
c.left, c.right = a, b
d = TreeNode(7)
e = TreeNode(3)
d.left, d.right = e, c

x = BSTIterator(d)