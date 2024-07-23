class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        if not root:
            return root
        curr, st = root, []
        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            curr.right, curr.left, curr = node, None, node
        return root


d, e, f = TreeNode(3), TreeNode(4), TreeNode(6)
a, b, c = TreeNode(1), TreeNode(2), TreeNode(5)
a.left, a.right = b, c
b.left, b.right = d, e
c.right = f

x = Solution().flatten(a)
print(x)