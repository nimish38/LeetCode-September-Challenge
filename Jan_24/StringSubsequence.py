class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s = list(set(list(s)))
        t = list(set(list(t)))

        i, j = 0, 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
        if i < len(s):
            return False
        return True

print(Solution().isSubsequence("axc",  "ahbgdc"))