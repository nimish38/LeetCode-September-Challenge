from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root) -> bool:
        lvl, flag = deque([root]), False
        while lvl:
            for _ in range(len(lvl)):
                node = lvl.popleft()
                if flag:
                    if node.left or node.right:
                        return False
                else:
                    if node.left:
                        lvl.append(node.left)
                    else:
                        flag = True

                    if node.right:
                        if flag:
                            return False
                        lvl.append(node.right)
                    else:
                        flag = True
        return True


a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
a.left, a.right, b.left, b.right, c.right = b, c, d, e, f
print(Solution().isCompleteTree(a))