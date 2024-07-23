class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        if not root:
            return root
        curr, st = TreeNode(0), [root]
        while st:
            node = st.pop()
            curr.next, curr = node, node
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
        return root