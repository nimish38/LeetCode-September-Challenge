from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars, s = {}, list(s)
        for i in range(len(s)):
            if s[i] in chars:
                s[i] = chars[s[i]]
            else:
                s[i] = t[i]
                chars[s[i]] = t[i]
        return ''.join(s) == t

print(Solution().isIsomorphic(s = "paperp", t = "titles"))