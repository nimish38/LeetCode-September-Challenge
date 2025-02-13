class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i, c in enumerate(s):
            if c in chars:
                chars[c][0] = [2, 1]
            else:
                chars[c] = [1, i]

        for i in chars:
            if chars[i][0] == 1:
                return chars[i][1]
        return -1


print(Solution().firstUniqChar(s = "loveleetcode"))