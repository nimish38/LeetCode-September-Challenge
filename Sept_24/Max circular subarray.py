class Solution:
    def maxSubarraySumCircular(self, nums):
        if len(nums) == 1:
            return nums[0]

        def Kadanes(arr):
            curr, bestSum = 0, arr[0]
            for i in range(len(arr)):
                curr += arr[i]
                bestSum = max(bestSum, curr)
                if curr < 0:
                    curr = 0
            return bestSum
        res = float('-inf')
        for _ in range(len(nums)):
            nums = [nums[-1]] + nums[:-1]
            sum = Kadanes(nums)
            res = max(res, sum)
        return res

print(Solution().maxSubarraySumCircular(nums = [2,-2,2,7,8,0]))