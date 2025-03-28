class Solution:
    def productExceptSelf(self, nums):
        left, right, ans = 1, 1, [1] * len(nums)
        for i, val in enumerate(nums):
            ans[i], left = left, left * val
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans


print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))