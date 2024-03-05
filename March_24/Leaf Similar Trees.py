class Solution:
    def leafs(self, root):
        stack, res = [root], []
        while stack:
            item = stack.pop()
            if not item.left and not item.right:
                res.append(item.val)
            else:
                if item.right:
                    stack.append(item.right)
                if item.left:
                    stack.append(item.left)
        return res


    def leafSimilar(self, root1, root2):
        # print(self.leafs(root1))
        # print(self.leafs(root2))
        return self.leafs(root1) == self.leafs(root2)
