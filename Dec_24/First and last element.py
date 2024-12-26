class Solution:
    def searchRange(self, nums, target):
        i, j, start, end = 0, len(nums), -1, -1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                start, end = mid
                if mid > 0 and nums[mid - 1] == target:
                    start = get_left(i, mid - 1)
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    end = get_right(mid + 1, j)
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return [start, end]

print(Solution().searchRange( nums = [5,7,7,8,8,10], target = 8))