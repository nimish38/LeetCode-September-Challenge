class Solution:
    def invertTree(self, root):
        st = [root]
        while st:
            node = st.pop()
            if node:
                node.left, node.right = node.right, node.left
                st.extend([node.left, node.right])
        return root
