class Solution:
    def maxSubArray(self, nums):
        n, curr, bestSum = len(nums), 0, nums[0]
        for val in nums:
            #step 1 - add num to curr sum
            curr += val
            #step2 - update bestSum
            bestSum = max(bestSum, curr)
            #step3 - check if curr nmm makes sum negative
            if curr < 0:
                curr = 0
        return bestSum

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))