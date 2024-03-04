# Definition for a binary tree node.
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        cnt, levels, kids = 1, [root], []
        while levels:
            node = levels.pop(0)
            if node.left:
                kids.append(node.left)
            if node.right:
                kids.append(node.right)
            if len(levels) == 0:
                levels = kids.copy()
                kids.clear()
                cnt += 1
        return cnt

