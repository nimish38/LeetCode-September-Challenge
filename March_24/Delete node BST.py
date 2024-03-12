class Solution:
    def findReplacement(self, node):
        while node and node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            inorder_succ = self.findReplacement(root.right)
            if not inorder_succ:
                if root.left:
                    root.val = root.left.val
                    del root.left
                else:
                    return
            else:
                root.val = inorder_succ.val
                inorder_succ.right = self.deleteNode(root.right, inorder_succ.val)
        return root