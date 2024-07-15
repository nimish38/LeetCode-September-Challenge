class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        queue, dep = [(root, 1)], 1
        while queue:
            for i in range(len(queue)):
                node, val = queue.pop(0)
                if dep < val:
                    dep = val
                if node.left:
                    queue.append((node.left, val + 1))
                if node.right:
                    queue.append((node.right, val + 1))
        return dep