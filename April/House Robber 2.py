class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)

        def dp(start, end):
            profit = [-1] * (n)
            profit[start] = nums[start]
            profit[start + 1] = max(nums[start], nums[start + 1])
            i = start + 2
            while(i <= end):
                profit[i] = max(nums[i] + profit[i - 2], profit[i - 1])
                i += 1

            if profit[-1] == -1:
                return profit[-2]
            return profit[-1]

        return max(dp(0, n - 2), dp(1, n - 1))

print(Solution().rob(nums = [1,2,3,1]))