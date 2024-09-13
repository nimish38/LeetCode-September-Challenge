import bisect
class Solution:
    def searchInsert(self, nums, target: int):
        if target in nums:
            return nums.index(target)
        return bisect.bisect_left(nums, target)

print(Solution().searchInsert(nums = [1,3,5,6], target = 7))

