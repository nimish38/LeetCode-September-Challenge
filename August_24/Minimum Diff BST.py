class Solution:
    def getMinimumDifference(self, root):
        diff, st = float('inf'), [root]
        while st:
            node = st.pop()
            if node.left:
                diff = min(diff, abs(node.val - node.left.val))
                st.append(node.left)
            if node.right:
                diff = min(diff, abs(node.val - node.right.val))
                st.append(node.right)

        return diff