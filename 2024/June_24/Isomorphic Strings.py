from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars, s = {}, list(s)
        for i in range(len(s)):
            if s[i] in chars:
                s[i] = chars[s[i]]
            else:
                chars[s[i]] = t[i]
                s[i] = t[i]
        return ''.join(s) == t and len(chars) == len(set(chars.values()))

print(Solution().isIsomorphic(s = "badc", t = "baba"))