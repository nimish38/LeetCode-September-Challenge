class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):

        def check(x, y):
            if not x and not y:
                return True
            if not x or not y or x.val != y.val:
                return False
            return check(x.left, y.left) and check(x.right, y.right)

        if not root and subRoot or not subRoot and root:
            return False
        st = [root]
        while st:
            node = st.pop()
            if node.val == subRoot.val and check(node, subRoot):
                return True
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return False