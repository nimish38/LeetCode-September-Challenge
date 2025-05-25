class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        def getHeight(node):
            if not node:
                return True, 0
            left, right = getHeight(node.left), getHeight(node.right)
            if not left[0] or not right[0]:
                return False, -1
            ans = 1 + max(left[1], right[1])
            val = True if abs(left[1] - right[1]) < 2 else False
            return val, ans
        return getHeight(root)[0]