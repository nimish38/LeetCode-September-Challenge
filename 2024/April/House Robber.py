class Solution:
    def rob(self, nums):
        profit = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            profit.append(max(nums[i - 1] + profit[i - 2], profit[i - 1]))
        return profit[-1]

print(Solution().rob([2,7,9,3,1]))