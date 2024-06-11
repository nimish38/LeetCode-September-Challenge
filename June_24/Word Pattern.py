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
        return len(mapping) == len(set(mapping.values()))

print(Solution().wordPattern(pattern = "abba", s = "dog dog dog dog"))