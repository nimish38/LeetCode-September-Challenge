class Solution:
    def findPeakElement(self, nums):
        if len(nums) < 3:
            return max(nums)
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

print(Solution().findPeakElement(nums = [1,2,1,3,5,6,4]))