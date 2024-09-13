class Solution:
    def searchInsert(self, nums, target: int):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start

print(Solution().searchInsert(nums = [1,3,5,6], target = 2))

