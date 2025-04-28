# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res, st = '', deque([root])
        while st:
            node = st.popleft()
            if not node:
                res += '#$'
            else:
                res += '#' + str(node.val)
                st.append(node.left)
                st.append(node.right)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
x = Codec().serialize(a)
print(x)