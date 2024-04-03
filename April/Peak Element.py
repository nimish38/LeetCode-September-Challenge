class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        low, high = 1, len(nums) - 2
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

print(Solution().findPeakElement(nums = [1,2,1,3,5,6,4]))