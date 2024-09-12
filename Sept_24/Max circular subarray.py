class Solution:
    def maxSubarraySumCircular(self, nums):
        first, last, curr, bestSum = True, False, 0, nums[0]
        for i in range(len(nums)):
            curr += nums[i]
            if curr > bestSum:
                bestSum = curr
                if i == len(nums) - 1:
                    last = True
            if curr < 0:
                curr = 0
                first = False
        if not first and last:
            return max(bestSum, bestSum + nums[0])
        return bestSum