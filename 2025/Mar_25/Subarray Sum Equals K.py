class Solution:
    def subarraySum(self, nums, k: int) -> int:
        freq, curr, cnt = {0: 1}, 0, 0
        for val in nums:
            curr += val
            if curr - k in freq:
                cnt += freq[curr - k]
            if curr in freq:
                freq[curr] += 1
            else:
                freq[curr] = 1
        return cnt


print(Solution().subarraySum(nums = [1,-1,0], k = 0))