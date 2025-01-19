# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        nodes, st, res = {}, [root]
        while st:
            value = st.pop()
            if value.val in nodes and checkDuplicate(value, nodes[value.val]):
                res.append(value)
                return res
            else:
                nodes[value.val] = value
                if value.left:
                    st.append(value.left)
                if value.right:
                    st.append(value.right)
        return res

