class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.nodes, self.ptr = [root], -1
        while root.left:
            self.nodes.append(root.left)
            root = root.left

    def next(self) -> int:
        node = self.nodes.pop()
        curr = node
        if curr.right:
            curr = curr.right
            self.nodes.append(curr)
            while curr.left:
                self.nodes.append(curr.left)
                curr = curr.left
        return node.val

    def hasNext(self) -> bool:
        if self.nodes:
            return True
        return False


a, b, c, d, e = TreeNode(7), TreeNode(3), TreeNode(15), TreeNode(9), TreeNode(20)
a.left, a.right, c.left, c.right = b, c, d, e
bSTIterator = BSTIterator(a)
print(bSTIterator.next())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())