class Solution:
    def subarraySum(self, nums, k: int) -> int:
        freq, curr, cnt = {0: 1}, 0, 0
        for val in nums:
            curr += val
            if curr - k in freq:
                cnt += freq[curr - k]
            freq[curr] = 1
        return cnt


print(Solution().subarraySum(nums = [1,2,3], k = 3))