from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        st, res = deque([root]), []
        while st:
            for _ in range(len(st)):
                node = st.popleft()
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            res.append(node.val)
        return res


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, b.right, c.right = b, c, e, d
print(Solution().rightSideView(a))