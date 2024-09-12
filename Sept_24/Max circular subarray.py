class Solution:
    def maxSubarraySumCircular(self, nums):
        if len(nums) == 1:
            return nums[0]

        last, curr, bestSum = False, 0, nums[1]
        for i in range(1, len(nums)):
            curr += nums[i]
            if curr > bestSum:
                bestSum = curr
                if i == len(nums) - 1:
                    last = True
            if curr < 0:
                curr = 0
        if last:
            bestSum = max(bestSum, bestSum + nums[0])

        curr, i = 0, 0
        while curr >= 0 and i < len(nums):
            curr += nums[i]
            bestSum = max(bestSum, curr)
            i += 1

        return bestSum

print(Solution().maxSubarraySumCircular(nums = [5,-3,5,-2,-2]))