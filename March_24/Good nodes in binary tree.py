class Solution:
    def findgood(self, node, lineage):
        cnt = leftCnt = rightCnt = 0
        if node.val >= lineage:
            cnt = 1
        if node.left:
            leftCnt = self.findgood(node.left, max(lineage, node.val))
        if node.right:
            rightCnt = self.findgood(node.right, max(lineage, node.val))

        return cnt + leftCnt + rightCnt

    def goodNodes(self, root):
        val = float('-inf')
        return self.findgood(root, val)