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
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        stack, cnt = [(root, [])], 0
        while stack:
            item = stack.pop()
            if item[0].val == targetSum:
                cnt += 1
            for i in range(len(item[1])):
                if item[0].val + sum(item[1][:i + 1]) == targetSum:
                    cnt += 1

            lineage = item[1].copy()
            lineage.insert(0, item[0].val)
            if item[0].right:
                stack.append((item[0].right, lineage))
            if item[0].left:
                stack.append((item[0].left, lineage))
        return cnt


z = TreeNode(3)
y = TreeNode(-2)
x = TreeNode(3)
x.left = z
x.right = y
m = TreeNode(1)
n = TreeNode(2)
n.right = m
o = TreeNode(5)
o.right = n
o.left = x
c = TreeNode(11)
b = TreeNode(-3)
b.right = c
a = TreeNode(10)
a.right = b
a.left = o

print(Solution().pathSum(a, 8))