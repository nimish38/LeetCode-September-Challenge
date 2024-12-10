from collections import defaultdict


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        positions, longest, order = defaultdict(list), 0, []
        for i in range(len(s)):
            positions[s[i]].append(i)
            if len(positions[s[i]]) > longest:
                longest = len(positions[s[i]])

        for val in positions:
            if len(positions[val]) == longest:
                order.append((positions[val][-1], val))
        order.sort()

        s = ''
        for a, b in order:
            s += b
        return s

print(Solution().lastNonEmptyString(s = "aabcbbca"))