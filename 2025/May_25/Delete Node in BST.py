class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        dummy = TreeNode(float('inf'), root)

        def findNode(node, parent):
            if not node or node.val == key:
                return (node, parent)
            if node.val < key:
                return findNode(node.right, node)
            return findNode(node.left, node)

        child, parent = findNode(root, dummy)
        if not child:
            return root

        if not child.left and not child.right:

            if child.val < parent.val:
                parent.left = None
                del  child
            else:
                parent.right = None
                del child

        elif not child.left or not child.right:
            if child.left:
                next = child.left
            else:
                next = child.right

            if child.val < parent.val:
                parent.left = next
                del  child
            else:
                parent.right = next
                del child

        else:
            next = child.left
            curr = next
            while curr.right:
                curr = curr.right
            curr.right = child.right
            if child.val < parent.val:
                parent.left = next
                del  child
            else:
                parent.right = next
                del child

        return dummy.right

a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(7)
a.left, a.right, b.left, b.right, c.right = b, c, d, e, f

print(Solution().deleteNode(a, 3))