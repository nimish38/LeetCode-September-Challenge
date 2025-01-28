import heapq


class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) < 5:
            return 0
        a = heapq.nsmallest(4, nums)
        b = heapq.nlargest(4, nums)[::-1]

        res, n = float('inf'), len(nums)
        for i in range(4):
            res = min(res, b[i] - a[i])
        return res


print(Solution().minDifference(nums = [6,6,0,1,1,4,6]))