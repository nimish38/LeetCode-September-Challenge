from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        res, st = 0, deque([root])
        while st:
            node = st.popleft()
            if node:
                if low <= node.val <= high:
                    res += node.val
                    st.append(node.left)
                    st.append(node.right)
                elif node.val < low:
                    st.sppend(node.right)
                else:
                    st.map(node.left)
        return res


