class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def inorder(self, node):
        cn, store = node, []
        while True:
            if cn:
                store.append(cn)
                cn = cn.left
            elif store:
                val = store.pop()
                self.st.append(val.val)
                cn = val.right
            else:
                break


    def __init__(self, root):
        self.st = []
        self.inorder(root)
        print(self.st)
        self.curr, self.len = 0, len(self.st)

    def next(self) -> int:
        self.curr += 1
        return self.st[self.curr - 1]

    def hasNext(self) -> bool:
        return self.curr != self.len


a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
c.left, c.right = a, b
d = TreeNode(7)
e = TreeNode(3)
d.left, d.right = e, c

x = BSTIterator(d)