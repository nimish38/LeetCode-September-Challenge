import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq._heapify_max(nums)
        return nums[k - 1]

print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))