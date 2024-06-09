from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = defaultdict(lambda : 0)
        for i in range(len(magazine)):
            letters[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in letters or letters[ransomNote] == 0:
                return False
            letters[ransomNote[i]] -= 1

        return True

print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))