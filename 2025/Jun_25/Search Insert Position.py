class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l + 1 if nums[l] < target else l

print(Solution().searchInsert(nums = [1,3,5,6], target = 5))