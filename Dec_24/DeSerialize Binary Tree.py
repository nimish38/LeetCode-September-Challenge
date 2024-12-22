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
                    if data[i] == 'L':
                        i += 1
                        lstr = ''
                        while data[i] != 'R':
                            lstr += data[i]
                            i += 1
                        if lstr != '#':
                            left = TreeNode(int(lstr))
                            node.left = left
                            st.append(left)
                    if data[i] == 'R':
                        i += 1
                        rstr =''
                        while i < n and data[i] != 'L':
                            rstr += data[i]
                            i += 1
                        if rstr != '#':
                            right = TreeNode(int(rstr))
                            node.right = right
                            st.append(right)
        return root


a, b, c, d, e = TreeNode(1),TreeNode(2), TreeNode(-13), TreeNode(4), TreeNode(5)
a.left, a.right, c.right, c.left = b, c, e, d
val = Codec().serialize(a)
tree = Codec().deserialize(val)
print(tree)