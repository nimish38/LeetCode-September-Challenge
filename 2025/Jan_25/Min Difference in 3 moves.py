import heapq


class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        diff, j = [], 3
        for i in range(1, len(nums)):
            heapq.heappush(diff, -1 * (nums[i] - nums[i - 1]))
        while diff[0] != 0 and j > 0:
            heapq.heappop(diff)
            j -= 1
        return -1 * sum(diff)


