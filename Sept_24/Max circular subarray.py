class Solution:
    def maxSubarraySumCircular(self, nums):
        if len(nums) == 1:
            return nums[0]

        def Kadanes():
            totsum, curr, bestSum = 0, 0, nums[0]
            for i in range(len(nums)):
                curr += nums[i]
                totsum += nums[i]
                bestSum = max(bestSum, curr)
                if curr < 0:
                    curr = 0
            return (bestSum, totsum)

        def Kadanes_min():
            curr, minSum = nums[0], nums[0]
            for i in range(1, len(nums)):
                curr = min(nums[i], curr + nums[i])
                minSum = min(minSum, curr)
            return minSum

        straight, total = Kadanes()
        circular = Kadanes_min()
        if straight > 0:
            return max(straight, total - circular)
        return straight
    
print(Solution().maxSubarraySumCircular(nums = [-3,-2,-3]))