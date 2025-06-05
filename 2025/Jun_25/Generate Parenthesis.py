class Solution(object):
    def generateParenthesis(self, n):
        open, close, res = n, n, []
        def solve(open, close, curr):
            if len(curr) == n * 2:
                res.append(curr)
                return
            if open < close:
                solve(open, close - 1, curr + ')')
            if open > 0:
                solve(open - 1, close, curr + '(')

        solve(open, close, '')
        return res

print(Solution().generateParenthesis(n = 3))