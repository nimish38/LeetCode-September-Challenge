class Solution:
    def rightSideView(self, root):
        res = []
        while root:
            res.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        return res