class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, best, res = len(s), 0, ''
        def expand(i, j):
            left, right = i, j
            while left > 0 and right < n -1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            return s[left: right + 1]

        for ind in range(n):
            odd = expand(ind, ind)
            if len(odd) > best:
                best, res = len(odd), odd

            if ind < n - 1 and s[ind] == s[ind + 1]:
                even = expand(ind, ind + 1)
                if len(even) > best:
                    best, res = len(even), even
        return res

print(Solution().longestPalindrome(s = "cbbd"))
