import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        arr = []
        for num in nums:
            if len(arr) < k:
                heapq.heappush(arr, num)
            elif len(arr) == k:
                heapq.heappushpop(arr, num)
        return heapq.heappop(arr)


print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))