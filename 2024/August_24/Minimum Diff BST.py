class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root):
        diff, st, curr = float('inf'), [], root
        prev = diff
        while curr:
            st.append(curr)
            curr = curr.left

        while st or curr:
            if not curr:
                curr = st.pop()
                # print(curr.val)
                diff = min(diff, abs(curr.val - prev))
                prev = curr.val
                curr = curr.right
            else:
                while curr:
                    st.append(curr)
                    curr = curr.left

        return diff

a, b, c = TreeNode(4), TreeNode(2), TreeNode(6)
a.left, a.right = b, c
b.left, b.right = TreeNode(1), TreeNode(3)


# a, b, c = TreeNode(1), TreeNode(3), TreeNode(2)
# a.right, b.left = b, c
print(Solution().getMinimumDifference(a))