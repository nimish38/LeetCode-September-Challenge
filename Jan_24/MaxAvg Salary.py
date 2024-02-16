class Solution:
    def findMaxAverage(self, nums, k):
        maxSum, curSum, last = sum(nums[:k]), sum(nums[:k]), nums[0]
        for i in range(1, len(nums) - k + 1):
            curSum = curSum - last + nums[i + k - 1]
            if curSum > maxSum:
                maxSum = curSum
            last = nums[i]
        return maxSum/k

print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))