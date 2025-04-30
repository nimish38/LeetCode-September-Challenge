class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.nodes, self.ptr = [], -1
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.nodes.append(node.val)
            if node.right:
                inorder(node.right)

    def next(self) -> int:
        self.ptr += 1
        return self.nodes[self.ptr]

    def hasNext(self) -> bool:
        if self.ptr + 1 < len(self.nodes):
            return True
        return False