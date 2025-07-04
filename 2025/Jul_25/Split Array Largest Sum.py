class Solution(object):
    def splitArray(self, nums, k):
        memo = [[-1] * (k + 1) for _ in range(len(nums))]
        def solve(ind, k):
            if k == 1:
                return sum(nums[ind:])
            if memo[ind][k] == -1:
                curr, res = 0, float('inf')
                for i in range(ind, len(nums) - k + 1):
                    curr += nums[i]
                    res = min(res, max(curr, solve(i + 1, k - 1)))
                    if curr > res:
                        break
                memo[ind][k] = res
            return memo[ind][k]
        return solve(0, k)

print(Solution().splitArray(nums = [7,2,5,10,8], k = 2))