class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.st.append(node.val)
        self.inorder(node.right)

    def __init__(self, root):
        self.st = []
        self.inorder(root)
        print(self.st)

    def next(self) -> int:
        return 1

    def hasNext(self) -> bool:
        return False


a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
c.left, c.right = a, b
d = TreeNode(7)
e = TreeNode(3)
d.left, d.right = e, c

x = BSTIterator(d)