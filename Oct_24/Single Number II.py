class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 2]:
                i += 3
            else:
                return nums[i]

print(Solution().singleNumber(nums = [0,1,0,1,0,1,99]))