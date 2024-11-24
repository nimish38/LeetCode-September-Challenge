import heapq


class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        heapq.heapify(nums)
        for _ in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, val * multiplier)

        return nums

print(Solution().getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
