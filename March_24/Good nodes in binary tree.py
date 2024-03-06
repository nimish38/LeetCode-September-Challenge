class Solution:
    def goodNodes(self, root):
        stack, cnt = [(root, float('-INF'))], 0
        while stack:
            node = stack.pop()
            curr, lineage = node[0], node[1]
            if curr.val >= lineage:
                cnt += 1
            if curr.right:
                stack.append((curr.right, max(lineage, curr.val)))
            if node[0].left:
                stack.append((curr.left, max(lineage, curr.val)))
        return cnt