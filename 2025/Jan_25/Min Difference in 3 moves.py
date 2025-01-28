class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        res, n = float('inf'), len(nums)
        for i in range(4):
            res = min(res, nums[n - 4 + i] - nums[i])
        return res


print(Solution().minDifference(nums = [6,6,0,1,1,4,6]))