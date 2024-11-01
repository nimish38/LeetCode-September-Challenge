class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        n, maxlen, res, memo = len(s), 0, '', []
        for _ in range(n + 1):
            memo.append([-1]*(n+1))
            memo[_][_] = True

        for l in range(2, n):
            for i in range(n - l + 1):
                for j in range(i, n):
                    if s[i] == s[j] and (l == 2 or memo[i + 1][j - 1]):
                        res, memo[i][j] = s[i: j + 1], True
                    else:
                        memo[i][j] = False
        return res

print(Solution().longestPalindrome(s = "babad"))