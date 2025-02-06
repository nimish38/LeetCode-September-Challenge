class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        n = len(nums)
        for length in range(1, n + 1):
            val = None
            for i in range(n - length + 1):
                if not val:
                    val = sum(nums[i: i + length])
                else:
                    val = val - nums[i - 1] + nums[i + length - 1]
                if val >= k:
                    return length
        return -1


print(Solution().shortestSubarray(nums = [2,-1,2], k = 3))
