from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(int)
        for i, c in enumerate(s):
            chars[c] += 1

        for i in chars:
            if chars[i] == 1:
                return i
        return -1


