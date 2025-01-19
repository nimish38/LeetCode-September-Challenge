# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        nodes, st, res = {}, [root]

        def checkDuplicate(a, b):
            x, y = [a], [b]
            while a and b:
                p, q = x.pop(), y.pop()
                if p.val != q.val:
                    return False
                if (not p.left and q.left) or (not q.left and p.left) or (not p.right and q.right) or (not q.right and p.right):
                    return False
                if p.left and q.left:
                    x.append(p.left)
                    y.append(q.left)
                if q.right and p.right:
                    x.append(p.right)
                    y.append(q.right)
            return True
        
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

