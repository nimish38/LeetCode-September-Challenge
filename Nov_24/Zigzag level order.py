class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        st, res, level, l2r = [root], [], [], True

        while st:
            n = len(st)
            for _ in range(n):
                node = st.pop()
                if l2r:
                    if node.left:
                        st.append(node.left)
                    if node.right:
                        st.append(node.right)
                else:
                    if node.right:
                        st.append(node.right)
                    if node.left:
                        st.append(node.left)

                level.append(node.val)
                l2r = not l2r
            res.append(level)
        return res

