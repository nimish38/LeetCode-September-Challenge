class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

print(Solution().singleNumber(nums = [4,1,2,1,2]))