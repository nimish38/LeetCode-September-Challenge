class Solution:
    def maxTotalReward(self, rewardValues) -> int:
        self.best, n = -1, len(rewardValues)
        rewardValues.sort()

        def solve(ind, curr):
            if ind >= n:
                self.best = max(self.best, curr)
                return 0
            take, skip = 0, 0
            if rewardValues[ind] > curr:
                take = solve(ind + 1, curr + rewardValues[ind])
            skip = solve(ind + 1, curr)
            return max(take, skip)

        solve(0, 0)
        return self.best

print(Solution().maxTotalReward(rewardValues = [1,6,4,3,2]))