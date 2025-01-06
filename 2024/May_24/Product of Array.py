class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * n
        res, i = [1] * n, 1
        left, right = nums[0], nums[-1]
        while i < n:
            res[i] *= left
            res[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
            i += 1
        return res

print(Solution().productExceptSelf(nums = [1,2,3,4]))

