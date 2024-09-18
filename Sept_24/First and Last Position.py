class Solution:
    def searchRange(self, nums, target: int):
        def binarySearch():
            start, end = 0, len(nums) - 1
            while start < end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        found = binarySearch()
        if found == -1:
            return [-1, -1]
        start, end = found, found
        while start > 0 and nums[start - 1] == target:
            start -= 1
        while end < len(nums) and nums[end + 1] == target:
            end += 1
        return [start, end]