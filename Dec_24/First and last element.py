class Solution:
    def searchRange(self, nums, target):
        i, start, end = 0, -1, -1
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                if start == -1:
                    start = i
                else:
                    end = i
            i += 1
        return [start, end]
