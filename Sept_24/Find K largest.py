import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq._heapify_max(nums)
        for _ in range(k - 1):
            heapq._heappop_max(nums)
        return heapq.heappop(nums)

print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))