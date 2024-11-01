class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, res, memo = len(s), '', []
        for _ in range(n):
            memo.append([-1]*(n))
            memo[_][_] = True
            res = s[_]

        for l in range(2, n):
            for i in range(n - l + 1):
                j = i + l -1
                if s[i] == s[j] and (l == 2 or memo[i + 1][j - 1]):
                    res, memo[i][j] = s[i: j + 1], True
                else:
                    memo[i][j] = False
        return res

print(Solution().longestPalindrome(s = "a"))