class Solution:
    def leafs(self, item, res):
        if not item.left and not item.right:
            res.append(item.val)
        else:
            if item.left:
                self.leafs(item.left, res)
            if item.right:
                self.leafs(item.right, res)
        return res


    def leafSimilar(self, root1, root2):
        # print(self.leafs(root1))
        # print(self.leafs(root2))
        return self.leafs(root1, []) == self.leafs(root2, [])
