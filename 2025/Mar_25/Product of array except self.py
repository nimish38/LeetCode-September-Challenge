class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        left, right = nums[0], nums[-1]
        for i in range(1, n):
            res[i] *= left
            res[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
        return res


print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))