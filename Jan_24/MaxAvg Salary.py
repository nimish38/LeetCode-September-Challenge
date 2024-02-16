class Solution:
    def findMaxAverage(self, nums, k):
        maxSum = float('-inf')
        for i in range(len(nums) - k + 1):
            cur = sum(nums[i:i+k])
            if cur > maxSum:
                maxSum = cur
        return maxSum/k
print(Solution().findMaxAverage([5], 1))