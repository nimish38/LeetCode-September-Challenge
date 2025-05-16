# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        st = [(root, float('-inf'), float('inf'))]
        while st:
            node, left, right = st.pop()
            if not left < node.val < right:
                return False
            if node.left:
                st.append((node.left, left, node.val))
            if node.right:
                st.append((node.right, node.val, right))
        return True

