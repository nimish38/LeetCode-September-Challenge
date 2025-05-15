class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))