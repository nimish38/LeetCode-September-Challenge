class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping, i = {}, 0
        for word in words:
            if pattern[i] in mapping:
                if mapping[pattern[i]] != word:
                    return False
            else:
                mapping[pattern[i]] = word
            i += 1
        return len(mapping) == len(set(mapping.values()))

print(Solution().wordPattern(pattern = "abb", s = "do dog dog"))