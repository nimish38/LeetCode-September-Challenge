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
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
ser = Codec().serialize(a)
print(ser)