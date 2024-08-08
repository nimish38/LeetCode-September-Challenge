class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        curr, st = root, []
        while curr:
            st.append(curr)
            curr = curr.left

        while st or curr:
            if not curr:
                curr = st.pop()
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                while curr:
                    st.append(curr)
                    curr = curr.left

a, b, c = TreeNode(3), TreeNode(4), TreeNode(1)
a.right, a.left = b, c
c.right = TreeNode(2)
print(Solution().kthSmallest(a, 3))