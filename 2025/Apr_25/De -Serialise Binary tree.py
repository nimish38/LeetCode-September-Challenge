# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        self.res = ''
        def build_str(node):
            self.res += '#' + str(node.val)
            if node.left:
                build_str(node.left)
            else:
                self.res += '#$'
            if node.right:
                build_str(node.right)
            else:
                self.res += '#$'
        build_str(root)
        return self.res


    def deserialize(self, data):
        data, self.ind = data.split('#'), 1
        
        def build_tree():
            if data[self.ind] != '$':
                node = TreeNode(int(data[self.ind]))
                self.ind += 1
                node.left = build_tree()
                self.ind += 1
                node.right = build_tree()
                return node
            return None
        
        return build_tree()

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
x = Codec().serialize(a)
print(x)
y = Codec().deserialize(x)
print(y)