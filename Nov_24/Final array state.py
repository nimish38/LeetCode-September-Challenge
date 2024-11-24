import heapq


class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        heapq.heapify(nums)
        for _ in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, val * multiplier)

        return nums


