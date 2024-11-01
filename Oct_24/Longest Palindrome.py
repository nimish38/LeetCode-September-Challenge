class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, maxlen, res, memo = len(s), 0, '', []
        for _ in range(n + 1):
            memo.append([-1]*(n+1))

        def solve(i, j):
            if i >= j:
                return True
            if memo[i][j] == -1:
                if s[i] == s[j]:
                    memo[i][j] = solve(i + 1, j - 1)
                else:
                    memo[i][j] = False
            return memo[i][j]

        for i in range(n):
            for j in range(i, n):
                if j + 1 - i > maxlen:
                    if solve(i, j):
                        maxlen, res = j + 1 - i, s[i: j + 1]
        return res

print(Solution().longestPalindrome(s = "babad"))