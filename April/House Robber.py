class Solution:
    def rob(self, nums):
        even, odd = 0, 0
        for i in range(len(nums)):
            if i % 2:
                odd += nums[i]
            else:
                even += nums[i]

        return max(even, odd)

print(Solution().rob([2,7,9,3,1]))