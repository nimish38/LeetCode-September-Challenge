class Solution(object):
    def makesquare(self, matchsticks):
        n, sums = len(matchsticks), sum(matchsticks)
        if sums % 4 != 0:
            return False
        sides, side = [0] * 4, sums // 4
        matchsticks.sort(reverse=True)
        def solve(i):
            if i == n:
                return True
            v = matchsticks[i]
            for j in range(4):
                if j > 0 and sides[j - 1] == sides[j]:
                    continue
                if sides[j] + v <= side:
                    sides[j] += v
                    if solve(i + 1):
                        return True
                    sides[j] -= v
            return False

        return solve(0)

print(Solution().makesquare(matchsticks = [5, 1, 2, 2, 4, 3, 3]))