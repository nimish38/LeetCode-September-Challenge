class Solution(object):
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums)
        memo = [-1] * len(nums)
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[-1]

print(Solution().rob(nums = [2,7,9,3,1]))