class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m

print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))