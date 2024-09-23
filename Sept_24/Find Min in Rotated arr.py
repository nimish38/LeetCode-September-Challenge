class Solution:
    def findMin(self, nums) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[end]

print(Solution().findMin(nums = [4,5,6,7,0,1,2]))