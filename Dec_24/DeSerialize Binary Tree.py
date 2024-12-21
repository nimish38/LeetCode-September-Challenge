# Definition for a binary tree node.
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

        res, lvl = str(root.val), [root]
        while lvl:
            node = lvl.pop(0)
            if node.left:
                res += 'L' + str(node.left.val)
                lvl.append(node.left)
            else:
                res += 'L#'
            if node.right:
                res += 'R' + str(node.right.val)
                lvl.append(node.right)
            else:
                res += 'R#'
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """