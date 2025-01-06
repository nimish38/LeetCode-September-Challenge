class Solution:
    def maxZigzag(self, node, rightFlag, cnt):
        if cnt > self.result:
            self.result = cnt
        if node.right:
            if rightFlag:
                self.maxZigzag(node.right, False, cnt + 1)
            else:
                self.maxZigzag(node.right, False, 1)
        if node.left:
            if not rightFlag:
                self.maxZigzag(node.left, True, cnt + 1)
            else:
                self.maxZigzag(node.left, True, 1)

    def longestZigZag(self, root):
        self.result = 0
        if root.left:
            self.maxZigzag(root.left, True, 1)
        if root.right:
            self.maxZigzag(root.right, False, 1)
        return self.result