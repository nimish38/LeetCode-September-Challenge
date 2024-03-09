class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAncestors(self, node):
        res = [node]
        while self.lineage[node]:
            res.append(self.lineage[node])
            node = self.lineage[node]
        return res


    def lowestCommonAncestor(self, root, p, q):
        self.lineage, stack = {}, [(root, None)]
        while p.val not in self.lineage or q.val not in self.lineage:
            item = stack.pop()
            if not item[1]:
                self.lineage[item[0].val] = None
            else:
                self.lineage[item[0].val] = item[1].val
            if item[0].right:
                stack.append((item[0].right, item[0]))
            if item[0].left:
                stack.append((item[0].left, item[0]))

        p = self.getAncestors(p.val)
        q = self.getAncestors(q.val)
        if len(p) == 0 or len(q) == 0:
            return root
        return [x for x in p if x in q][0]


a = TreeNode(3)
a.left = TreeNode(5)
a.right = TreeNode(1)
a.left.left = TreeNode(6)
a.left.right = TreeNode(2)
a.left.right.left = TreeNode(7)
a.left.right.right = TreeNode(4)

print(Solution().lowestCommonAncestor(a, a.left, a.left.right.right))