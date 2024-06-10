from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s, t = Counter(s).values(), Counter(t).values()
        s, t = sorted(list(s)), sorted(list(t))
        # print(s, t)
        return s == t

print(Solution().isIsomorphic(s = "paper", t = "title"))