# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insertBST(self, curr, new):
        if new.val < curr.val:
            if curr.left:
                self.insert(curr.left, new)
            else:
                curr.left = new
        else:
            if curr.right:
                self.insert(curr.right, new)
            else:
                curr.right = new

    def addElement(self, node):
        if not self.root:
            self.root = node
        else:
            self.insert(self.root, node)
    
    def getHead(self):
        return self.root

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

BinaryTree = Tree()
nodes = []
