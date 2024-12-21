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
        if not root:
            return ''
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

        if data == '':
            return None
        top, i = data[0], 0
        if data[0] == '-':
            top = int(data[1]) * -1
            i = i + 1
        root = TreeNode(top)
        st, i, n = [root], i + 1, len(data)
        while st:
            for _ in range(len(st)):
                node = st.pop(0)
                if i < n:
                    l = data[i + 1]
                    if l != '#':
                        if l == '-':
                            l = int(data[i + 2]) * -1
                            i += 1
                        left = TreeNode(l)
                        node.left = left
                        st.append(left)
                    r = data[i + 3]
                    if r != '#':
                        if r == '-':
                            r = int(data[i + 4]) * -1
                            i += 1
                        right = TreeNode(r)
                        node.right = right
                        st.append(right)
                i += 4
        return root


a, b, c, d, e = TreeNode(-1),TreeNode(0), TreeNode(1), TreeNode(-4), TreeNode(5)
a.left, a.right = b, c
val = Codec().serialize(a)
tree = Codec().deserialize(val)
print(tree)