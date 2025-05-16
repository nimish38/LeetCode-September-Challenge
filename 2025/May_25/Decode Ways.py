class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        memo = [-1] * (n + 1)
        memo[n] = 1

        for ind in range(n - 1, -1, -1):
            if s[ind] == '0':
                memo[ind] = 0
            else:
                memo[ind] = memo[ind + 1]
                if ind < n - 1 and ( s[ind] == '1' or (s[ind] == '2' and s[ind + 1] <= '6')):
                    memo[ind] += memo[ind + 2]
        return memo[0]

print(Solution().numDecodings(s = "226"))