class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.cnt, self.res = 0, -1
        def inorder(node):
            if self.cnt > k:
                return
            if node.left:
                inorder(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
                return
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.res

a, b, c, d = TreeNode(3), TreeNode(2), TreeNode(1), TreeNode(4)
a.left, a.right, c.right = c, d, b
print(Solution().kthSmallest(a, 1))