class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, res = len(nums), 1
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))