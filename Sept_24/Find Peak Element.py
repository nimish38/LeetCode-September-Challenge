class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[1] > nums[0]:
            return 1
        if nums[-1] > nums[-2]:
            return n - 1
