class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        st, height = [(root, 1)], -1
        while st:
            node, val = st.pop()
            height = max(height, val)
            if node.left:
                st.append((node.left, val + 1))
            if node.right:
                st.append((node.right, val + 1))
        return height
