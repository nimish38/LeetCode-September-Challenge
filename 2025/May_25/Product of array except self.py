class Solution(object):
    def productExceptSelf(self, nums):
        left, right, res, n = nums[0], nums[-1], [1] * len(nums), len(nums)
        for i in range(1, len(nums)):
            res[i] *= left
            res[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
        return res

print(Solution().productExceptSelf(nums = [1,2,3,4]))