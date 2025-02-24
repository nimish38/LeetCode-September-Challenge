class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cnt, n, curr,  prefix_sum = 0, len(nums), 0, {0: 1}
        for i in range(n):
            curr += nums[i]
            if curr - k in prefix_sum:
                cnt += prefix_sum[curr - k]
            if curr in prefix_sum:
                prefix_sum[curr] += 1
            else:
                prefix_sum[curr] = 1
        return cnt


print(Solution().subarraySum(nums = [1,2,3], k = 3))
