class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, maxlen, res = len(s), 0, ''

        def solve(i, j):
            if i >= j:
                return True
            if s[i] == s[j]:
                return solve(i + 1, j - 1)
            else:
                return False

        for i in range(n):
            for j in range(i, n):
                if j + 1 - i > maxlen:
                    if solve(i, j):
                        maxlen, res = j + 1 - i, s[i: j + 1]
        return res

print(Solution().longestPalindrome(s = "babad"))