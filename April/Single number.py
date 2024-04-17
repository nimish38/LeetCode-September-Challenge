class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        return xor

print(Solution().singleNumber(nums = [4,4,2,1,2]))