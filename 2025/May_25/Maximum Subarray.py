class Solution:
    def maxSubArray(self, nums):
        curr, best = float('-inf'), float('-inf')
        for num in nums:
            if curr + num > num:
                curr += num
            else:
                curr = num
            best = max(best, curr)
        return best

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
