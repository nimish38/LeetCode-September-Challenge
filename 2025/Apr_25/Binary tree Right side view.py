from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
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