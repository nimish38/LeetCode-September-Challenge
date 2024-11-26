class Solution:
    def maxSum(self, nums, m: int, k: int) -> int:
        unique, curr, maxsum, n = set(), 0, 0,  len(nums)
        for i in range(n - k + 1):
            if curr == 0:
                unique = set(nums[i: i + k])
                if len(unique) >= m:
                    curr = maxsum = sum(nums[i:i+k])

            else:
                unique.remove(nums[i - 1])
                curr -= nums[i - 1]
                unique.add(nums[i + k])
                curr += nums[i + k]

                if len(unique) >= m:
                    maxsum = max(curr, maxsum)

        return maxsum

