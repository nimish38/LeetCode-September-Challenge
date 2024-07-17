class Solution:
    def invert(self, node):
        if node.left or node.right:
            node.left, node.right = node.right, node.left
        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)
        return node


    def invertTree(self, root):
        if not root:
            return None
        return self.invert(root)