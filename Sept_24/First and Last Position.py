class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = binarySearch()
        if found == -1:
            return [-1, -1]
        start, end = found, found
        while start > 0 and nums[start - 1] == nums[found]:
            start -= 1
        while end < len(nums) and nums[end + 1] == nums[found]:
            end += 1
        return [start, end]