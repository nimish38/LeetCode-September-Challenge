# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        if not root: return ""

        string = []
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur:
                string.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                string.append('#')

        return ','.join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        if not data: return None
        data = data.split(',')
        q = deque()
        root = TreeNode(int(data[0]))
        q.append(root)
        i = 1

        while i < len(data):
            cur = q.popleft()
            if data[i] != '#':
                cur.left = TreeNode(int(data[i]))
                q.append(cur.left)
            i += 1
            if data[i] != '#':
                cur.right = TreeNode(int(data[i]))
                q.append(cur.right)
            i += 1

        return root

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
x = Codec().serialize(a)
print(x)
y = Codec().deserialize(x)
print(y)