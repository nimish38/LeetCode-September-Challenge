# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        def node2str(node):
            if not node:
                return '#'
            return str(node.val) + '|' + node2str(node.left) + '|' + node2str(node.right)
        return node2str(root)

    def deserialize(self, data):
        data, self.val = data.split('|'), 0
        def str2node():
            if data[self.val] == '#':
                return None
            node = TreeNode(data[self.val])
            self.val += 1
            node.left = str2node()
            self.val += 1
            node.right = str2node()
            return node
        return str2node()


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
ser = Codec().serialize(a)
print(ser)
des = Codec().deserialize(ser)
print(des)