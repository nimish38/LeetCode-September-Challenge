class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        memo, a, b, c = [0] * (n + 1), 0, 0, 0

        for i in range(n - 1, -1, -1):
            res = float('-inf')
            res = max(res, stoneValue[i] - a)
            if i + 2 <= n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] - b)
            if i + 3 <= n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - c)
            memo[i] = res
            c, b, a = b, a, res

        val = memo[0]
        if val > 0:
            return 'Alice'
        if val < 0:
            return 'Bob'
        return 'Tie'

print(Solution().stoneGameIII(stoneValue = [-1,-2,-3]))