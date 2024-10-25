class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, last, memo = len(nums), -1, []
        for _ in range(n + 1):
            memo.append([-1] * (n + 1))

        def solve(ind, last):
            if ind == n:
                return 0
            if memo[ind][last] == -1:
                take = 0
                if last == -1 or nums[ind] > nums[last]:
                    take = 1 + solve(ind + 1, ind)
                skip = solve(ind + 1, last)
                memo[ind][last] = max(take, skip)
            return memo[ind][last]

        return solve(0, last)

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))