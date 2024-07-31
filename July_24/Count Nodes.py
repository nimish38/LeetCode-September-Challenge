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
        return i - 1


