class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

a, b, c = TreeNode(4), TreeNode(2), TreeNode(6)
a.left, a.right = b, c
b.left, b.right = TreeNode(1), TreeNode(3)