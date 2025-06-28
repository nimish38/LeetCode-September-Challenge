class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

print(Solution().singleNumber(nums = [2,1, 4, 2,1]))