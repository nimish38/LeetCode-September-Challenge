class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        if not root:
            return
        nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        root.left = None
        root.right = None
        temp = root
        for i in range(1, len(nodes)):
            newNode = TreeNode(nodes[i])
            temp.right = newNode
            temp = temp.right


d, e, f = TreeNode(3), TreeNode(4), TreeNode(6)
a, b, c = TreeNode(1), TreeNode(2), TreeNode(5)
a.left, a.right = b, c
b.left, b.right = d, e
c.right = f

x = Solution().flatten(a)
print(x)