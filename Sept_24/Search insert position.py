import bisect
class Solution:
    def searchInsert(self, nums, target: int):
        if target in nums:
            return nums.index(target)
        return bisect.bisect_left(nums, target)

