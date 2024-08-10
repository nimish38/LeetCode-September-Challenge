class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        curr, st = root, []
        while curr:
            st.append(curr)
            curr = curr.left

        inorder = []
        while st or curr:
            if not curr:
                curr = st.pop()
                inorder.append(curr.val)
                curr = curr.right
            else:
                while curr:
                    st.append(curr)
                    curr = curr.left
        if len(inorder) == len(set(inorder)) and inorder == sorted(inorder):
            return True
        return False

a, b, c = TreeNode(5), TreeNode(4), TreeNode(1)
a.right, a.left = b, c
b.left, b.right = TreeNode(3), TreeNode(2)

# a, b = TreeNode(0), TreeNode(1)
# a.right = b
print(Solution().isValidBST(a))