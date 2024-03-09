class Solution:
    def getAncestors(self, node):
        res = set()
        while self.lineage[node]:
            res.add(self.lineage[node])
            node = self.lineage[node]
        return res


    def lowestCommonAncestor(self, root, p, q):
        self.lineage, stack = {}, [(root, None)]
        while p not in self.lineage and q not in self.lineage:
            item = stack.pop()
            self.lineage[item[0]] = item[1]
            if item[0].right:
                stack.append((item[0].right, item[0]))
            if item[0].left:
                stack.append((item[0].left, item[0]))

        p = self.getAncestors(p)
        q = self.getAncestors(q)
        return p.intersection(q)[0]