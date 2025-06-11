class Solution(object):
    def goodNodes(self, root):
        st, cnt = [(root, float('-inf'))], 0
        while st:
            node, parent = st.pop()
            if parent <= node.val:
                cnt += 1
            if node.right:
                st.append((node.right, max(parent, node.val)))
            if node.left:
                st.append((node.left, max(parent, node.val)))
        return cnt