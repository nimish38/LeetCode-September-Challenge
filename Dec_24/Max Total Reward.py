class Solution:
    def maxTotalReward(self, rewardValues) -> int:
        self.best, n = -1, len(rewardValues)
        rewardValues.sort()

        def solve(ind, curr):
            if ind >= n:
                return 0
            take, skip = 0, 0
            if rewardValues[ind] > curr:
                take = rewardValues[ind] + solve(ind + 1, curr + rewardValues[ind])
            skip = solve(ind + 1, curr)
            return max(take, skip)

        return solve(0, 0)

print(Solution().maxTotalReward(rewardValues = [1,6,4,3,2]))