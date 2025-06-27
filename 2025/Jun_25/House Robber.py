class Solution(object):
    def rob(self, nums):
        memo = [-1] * len(nums)
        def solve(i):
            if i >= len(nums):
                return 0
            if memo[i] == -1:
                memo[i] = max(solve(i + 1), nums[i] + solve(i + 2))
            return memo[i]
        return solve(0)

print(Solution().rob(nums = [2,7,9,3,1]))