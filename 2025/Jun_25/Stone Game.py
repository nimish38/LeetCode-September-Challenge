class Solution(object):
    def stoneGame(self, piles):
        l, r = 0, len(piles) - 1
        memo = [[-1] * (r + 1) for _ in range(r + 1)]
        def solve(l, r):
            if l > r:
                return 0
            if memo[l][r] == -1:
                first = piles[l] - solve(l + 1, r)
                last = piles[r] - solve(l, r - 1)
                memo[l][r] = max(first, last)
            return memo[l][r]
        return solve(l, r) > 0

print(Solution().stoneGame(piles = [3,7,2,3]))