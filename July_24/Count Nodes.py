class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        st, i = [root], 0
        while i < len(st):
            node, i = st[i], i + 1
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return i

m, n, o = TreeNode(4), TreeNode(5), TreeNode(6)
p, q = TreeNode(2), TreeNode(3)
p.left, p.right, q.left = m, n, o
r = TreeNode(1)
r.left, r.right = p, q
print(Solution().countNodes(r))