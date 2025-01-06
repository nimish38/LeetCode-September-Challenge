from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

print(Solution().isAnagram(s = "anagram", t = "nagaram"))