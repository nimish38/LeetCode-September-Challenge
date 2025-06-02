class Solution(object):
    def findTargetSumWays(self, nums, target):
        n, s = len(nums), sum(nums)
        memo = [[-1] * ((s * 2) + 1) for _ in range(n)]
        def solve(i, val):
            if i == n:
                if val == target:
                    return 1
                return 0
            key = val + s
            print(i, key)
            if memo[i][key] == -1:
                memo[i][key] = solve(i + 1, val + nums[i]) + solve(i + 1, val - nums[i])
            return memo[i][key]
        return solve(0, 0)

print(Solution().findTargetSumWays(nums = [1,0], target = 1))