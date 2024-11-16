class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        st, res, level, l2r = [root], [], [], True

        while st:
            n = len(st)
            for _ in range(n):
                node = st.pop(0)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
                level.append(node.val)
            if not l2r:
                level = level[::-1]
            res.append(list(level))
            level.clear()
            l2r = not l2r
        return res


a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
c.left, c.right = d, e
a.left, a.right = b, c
print(Solution().zigzagLevelOrder(a))