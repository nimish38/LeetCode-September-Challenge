from collections import defaultdict


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        positions, longest = defaultdict(list), 0
        for i in range(len(s)):
            positions[s[i]].append(i)
            if len(positions[s[i]]) > longest:
                longest = len(positions[s[i]])
        print(positions, longest)


print(Solution().lastNonEmptyString(s = "aabcbbca"))