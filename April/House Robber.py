class Solution:
    def rob(self, nums):
        def steal(ind):
            if ind >= len(nums):
                return 0
            if profit[ind] == -1:
                profit[ind] = max(nums[ind] + steal(ind + 2), steal(ind + 1))
            return profit[ind]
        profit = [-1] * len(nums)
        return steal(0)


print(Solution().rob([2,7,9,3,1]))