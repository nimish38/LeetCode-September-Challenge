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
