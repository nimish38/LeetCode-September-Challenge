from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        if set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values()):
            return True
        return False

print(Solution().closeStrings('abc', 'acb'))