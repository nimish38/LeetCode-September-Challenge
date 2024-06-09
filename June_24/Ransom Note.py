from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = Counter(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] not in letters or letters[ransomNote[i]] == 0:
                return False
            letters[ransomNote[i]] -= 1

        return True

print(Solution().canConstruct(ransomNote = "aaa", magazine = "aab"))