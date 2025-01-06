from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = Counter(magazine)
        rans = Counter(ransomNote)

        for char in rans:
            if char not in letters or rans[char] > letters[char]:
                return False

        return True

print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))