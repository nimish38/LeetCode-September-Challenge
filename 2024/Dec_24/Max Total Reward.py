class Solution:
    def maxTotalReward(self, rewardValues) -> int:
        memo, n = [], len(rewardValues)
        rewardValues.sort()
        for _ in range(n):
            memo.append([-1] * rewardValues[-1] * 2)

        def solve(ind, curr):
            if ind >= n:
                return 0
            if memo[ind][curr] == -1:
                take, skip = 0, 0
                if rewardValues[ind] > curr:
                    take = rewardValues[ind] + solve(ind + 1, curr + rewardValues[ind])
                skip = solve(ind + 1, curr)
                memo[ind][curr] = max(take, skip)
            return memo[ind][curr]

        return solve(0, 0)

print(Solution().maxTotalReward(rewardValues = [1,6,4,3,2]))