class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, maxlen, res = len(s), 0, ''
        for i in range(n):
            for j in range(i, n):
                if j + 1 - i > maxlen:
                    x = s[i:j+1]
                    if x == x[::-1]:
                        maxlen, res = len(x), x
        return res

print(Solution().longestPalindrome(s = "babad"))