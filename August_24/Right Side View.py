class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return root
        st, res = [root], []
        while st:
            res.append(st[-1].val)
            for _ in range(len(st)):
                node = st.pop()
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
        return res

a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left, a.right = b, c
b.left = TreeNode(4)
print(Solution().rightSideView(a))