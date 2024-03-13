class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLefttmost(self, node):
        while node and node.left:
            node = node.left
        return node

    def successor(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        lastElem = self.findLefttmost(node.right)
        lastElem.left = node.left
        return node.right

    def deleteNode(self, root, key):
        if not root:
            return
        if root.val == key:
            return self.successor(root)
        curr = root
        while curr:
            if key < curr.val and curr.left:
                if curr.left.val == key:
                    curr.left = self.successor(curr.left)
                    break
                else:
                    curr = curr.left

            elif key > curr.val and curr.right:
                if curr.right.val == key:
                    curr.right = self.successor(curr.right)
                    break
                else:
                    curr = curr.right
        return curr

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(6)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)
a.right.right =TreeNode(7)

res = Solution().deleteNode(a,3)
print(res)