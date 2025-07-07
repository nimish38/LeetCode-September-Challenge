class Solution(object):
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - k
        while l < r:
            mid = (r + l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l : l + k]

print(Solution().findClosestElements(arr = [1,1,2,2,2,2,2,3,3], k = 3, x = 3))