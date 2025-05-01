class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for j in range(n, -1, -1):
            for i in range(n - j + 1):
                curr = s[i: i + j]
                # print(curr)
                if curr == curr[::-1]:
                    return curr
        return ''

print(Solution().longestPalindrome(s = "cbbd"))
