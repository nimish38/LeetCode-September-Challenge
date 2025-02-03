class Solution:
    def countSubstrings(self, s: str) -> int:
        self.cnt, n = 0, len(s)

        def check(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                self.cnt += 1
                i -= 1
                j += 1

        for i in range(n):
            check(i, i)
            check(i, i + 1)
        return self.cnt


print(Solution().countSubstrings(s = "abc"))