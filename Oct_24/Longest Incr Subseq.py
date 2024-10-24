class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, last = len(nums), float('-inf')
        memo = [-1] * (n + 1)

        def solve(ind, last):
            if ind == n:
                return 0
            if memo[ind] == -1:
                take = 0
                if nums[ind] > last:
                    take = 1 + solve(ind + 1, nums[ind])
                skip = solve(ind + 1, last)
                memo[ind] = max(take, skip)
            return memo[ind]

        solve(0, last)
        return memo[n]

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))