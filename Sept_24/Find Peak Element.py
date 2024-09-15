class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[1] > nums[0]:
            return 1
        if nums[-1] > nums[-2]:
            return n - 1
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        return start

