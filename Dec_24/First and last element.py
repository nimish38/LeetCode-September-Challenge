class Solution:
    def searchRange(self, nums, target):
        i, start, end = 0, -1, -1
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                if start == -1:
                    start = end = i
                else:
                    end = i
            i += 1
        return [start, end]


print(Solution().searchRange( nums = [5,7,7,8,8,10], target = 8))