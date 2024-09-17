class Solution:
    def search(self, nums, target: int):
        n = len(nums)
        if n == 1:
            return nums[0] == target

        def findPivot():
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

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
        if pivot != -1:
            left = binarySearch(0, pivot)
            if left == -1:
                right = binarySearch(pivot + 1, n - 1)
                return right
            return left
        return binarySearch(0, n - 1)

print(Solution().search(nums = [3,4,5,6,7], target = 0))
