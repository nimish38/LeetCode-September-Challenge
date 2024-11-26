class Solution:
    def maxSum(self, nums, m: int, k: int) -> int:
        unique, curr, maxsum, n = set(), 0, 0,  len(nums)
        for i in range(n - k + 1):
            if curr == 0:
                unique = set(nums[i: i + k])
                if len(unique) >= m:
                    curr = maxsum = sum(nums[i:i+k])
            else:
                unique = set(nums[i: i + k])
                curr = curr - nums[i - 1] + nums[i + k - 1]
                if len(unique) >= m:
                    maxsum = max(curr, maxsum)
        return maxsum

print(Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3))