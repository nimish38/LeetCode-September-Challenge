class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder = []):
        # do the following
#   make first node from preorder as root
#   find that node in inorder
#   recursively call all left nodes in inorder as root.left
# recursively call all right nodes in inorder as root.right
#  repeat till empty

