class Solution:
    def rob(self, nums):
        def steal(ind):
            if ind >= len(nums):
                return 0
            return max(nums[ind] + steal(ind + 2), steal(ind + 1))
        return steal(0)


print(Solution().rob([2,7,9,3,1]))