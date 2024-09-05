# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def build(low, high):
            if low > high:
                return None
            mid = (high + low) // 2
            root = TreeNode(nums[mid])
            root.left = build(low, mid - 1)
            root.right = build(mid + 1, high)
            return root
        return build(0, len(nums)-1)

x = Solution().sortedArrayToBST(nums = [-10,-3,0,5,9])
print(x.val)