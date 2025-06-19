class Solution(object):
    def minExtraChar(self, s, dictionary):
        dictionary, n = {word: 1 for word in dictionary}, len(s)
        memo = [-1] * n
        def solve(ind):
            if ind >= n:
                return 0
            if memo[ind] == -1:
                res, val = n, ''
                for i in range(ind, n):
                    val += s[i]
                    if val in dictionary:
                        res = min(res, solve(i + 1))
                res = min(res, 1 + solve(ind + 1))
                memo[ind] = res
            return memo[ind]
        return solve(0)

print(Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))