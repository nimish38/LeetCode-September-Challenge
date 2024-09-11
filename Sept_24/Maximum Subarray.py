class Solution:
    def maxSubArray(self, nums):
        n, bestSum = len(nums), float('-inf')
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                bestSum = max(bestSum, sum)
        return bestSum

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))