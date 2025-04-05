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
            if low <= node.val <= high:
                res += node.val
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            elif node.val < low:
                if node.right:
                    st.append(node.right)
            else:
                if node.left:
                    st.append(node.left)
        return res


a, b, c, d, e, f = TreeNode(10), TreeNode(5), TreeNode(15), TreeNode(3), TreeNode(7), TreeNode(18)
a.left, a.right, b.left, b.right, c.right = b, c, d, e, f
print(Solution().rangeSumBST(a, 7, 15))