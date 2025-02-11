from collections import Counter


class Solution:
    def deleteAndEarn(self, nums) -> int:
        cnt = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        memo = [-1] * n

        def solve(i):
            if i >= n:
                return 0
            if memo[i] == -1:
                take = nums[i] * cnt[nums[i]]
                if i < n - 1 and nums[i] != nums[i + 1] - 1:
                    take += solve(i + 1)
                else:
                    take += solve(i + 2)
                skip = solve(i + 1)
                memo[i] = max(take, skip)
            return memo[i]

        return solve(0)


print(Solution().deleteAndEarn(nums = [2,2,3,3,3,4]))