class Solution:
    def getDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def maxDepth(self, root):
        if not root:
            return 0
        return self.getDepth(root)