class Solution:
    def isSymmetric(self, root) -> bool:
        st = [(root.left, root.right)]
        while st:
            p, q = st.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            st.extend([(p.left, q.right), (p.right, q.left)])
        return True
    