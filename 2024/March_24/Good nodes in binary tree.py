class Solution:
    def findgood(self, root, lineage):
        if not root:
            return
        if root.val >= lineage:
            lineage = root.val
            self.cnt += 1

        self.findgood(root.left, lineage)
        self.findgood(root.right, lineage)

    def goodNodes(self, root):
        if not root:
            return 0
        self.cnt = 0
        self.findgood(root, float('-INF'))
        return self.cnt