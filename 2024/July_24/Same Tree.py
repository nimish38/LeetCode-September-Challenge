class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        x, y = [p], [q]
        while x and y:
            a, b = x.pop(), y.pop()
            if not a and not b:
                continue
            if (not a and b) or (a and not b):
                return False
            if (a and b) and a.val != b.val:
                return False
            x.extend([a.left, a.right])
            y.extend([b.left, b.right])
        if x or y:
            return False
        return True


x, y = TreeNode(2), TreeNode(3)
z = TreeNode(1, x, y)

a, b = TreeNode(2), TreeNode(3)
c = TreeNode(1, a, b)

print(Solution().isSameTree(z, c))