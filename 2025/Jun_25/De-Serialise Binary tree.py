class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return 'N'
        return str(root.val) + '#' + self.serialize(root.left) + '#' + self.serialize(root.right)

    def deserialize(self, data):
        self.ptr, data = 0 , data.split('#')
        def solve():
            if data[self.ptr] == 'N':
                return None
            node = TreeNode(data[self.ptr])
            self.ptr += 1
            node.left = solve()
            self.ptr += 1
            node.right = solve()
            return node
        return solve()

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
x = Codec().serialize(a)
z = Codec().deserialize(x)
print(z)