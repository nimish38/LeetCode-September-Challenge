class Solution:
    def rob(self, nums):
        n = len(nums)
        profit = [-1]*(n - 1)
        sec_profit = [-1]*(n)

        def dp(ind, end, arr):
            if ind > end:
                return 0
            if arr[ind] == -1:
                arr[ind] = max(nums[ind] + dp(ind + 2, end, arr), dp(ind + 1, end, arr))
            return arr[ind]

        return max(dp(0, n-2, profit), dp(1, n-1, sec_profit))

print(Solution().rob(nums = [1,2,3,1]))