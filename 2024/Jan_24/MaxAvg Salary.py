class Solution:
    def findMaxAverage(self, nums, k):
        maxSum, curSum = sum(nums[:k]), sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            curSum = curSum - nums[i - 1] + nums[i + k - 1]
            if curSum > maxSum:
                maxSum = curSum
        return maxSum/k

print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))