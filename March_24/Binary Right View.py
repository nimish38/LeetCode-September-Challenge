class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        final = {}
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            final[level] = node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return final.values()

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
print(Solution().rightSideView(a))