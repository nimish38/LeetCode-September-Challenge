class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] == nums[i + 2]:
                i += 3
            else:
                return nums[i]

print(Solution().singleNumber())