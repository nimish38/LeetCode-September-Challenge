class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def solve(str, open, close):
            if open == 0 and close == 0:
                res.append(str)
                return
            if open > 0:
                solve(str + '(', open - 1, close)
            if close > open:
                solve(str + ')', open, close - 1)

        solve('(', n - 1, n)
        return res

print(Solution().generateParenthesis(1))
