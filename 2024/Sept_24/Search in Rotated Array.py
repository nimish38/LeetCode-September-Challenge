class Solution:
    def search(self, nums, target: int):
        n = len(nums)
        if n == 1:
            return -1 if nums[0] != target else 0

        def findPivot():
            start, end = 0, n - 1
            while start < end:
                mid = (start + end) // 2
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid
            return end

        def binarySearch(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        pivot = findPivot()
        left = binarySearch(0, pivot - 1)
        if left == -1:
            right = binarySearch(pivot, n - 1)
            return right
        return left

print(Solution().search(nums = [6,7,8,1,2,3,4,5], target = 6))
