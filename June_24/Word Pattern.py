class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping, i = {}, 0
        for word in s.split():
            if pattern[i] in mapping:
                if mapping[pattern[i]] != word:
                    return False
            else:
                mapping[pattern[i]] = word
            i += 1
        return True

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dogs"))