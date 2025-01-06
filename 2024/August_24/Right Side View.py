class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return root
        st, res, i = [root], [], 0
        while i < len(st):
            res.append(st[-1].val)
            moves = len(st)
            for _ in range(i, moves):
                node = st[_]
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
                i += 1
        return res

a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left, a.right = b, c
b.right, c.right = TreeNode(5), TreeNode(4)
print(Solution().rightSideView(a))