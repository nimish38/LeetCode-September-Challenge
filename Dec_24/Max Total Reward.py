class Solution:
    def maxTotalReward(self, rewardValues) -> int:
        n = len(rewardValues)
        memo = [-1] * n
        rewardValues.sort()

        def solve(ind, curr):
            if ind >= n:
                return 0
            if memo[ind] == -1:
                take, skip = 0, 0
                if rewardValues[ind] > curr:
                    take = rewardValues[ind] + solve(ind + 1, curr + rewardValues[ind])
                skip = solve(ind + 1, curr)
                memo[ind] = max(take, skip)
            return memo[ind]

        return solve(0, 0)

print(Solution().maxTotalReward(rewardValues = [1,6,4,3,2]))