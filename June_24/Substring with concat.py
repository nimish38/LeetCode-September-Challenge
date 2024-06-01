import itertools
class Solution:
    def findSubstring(self, s: str, words):
        perms = list(itertools.permutations(words))
        i, n, res = 0, len(perms[0]), []
        while i < len(s) - n + 1:
            if s[i: i + n] in perms:
                res.append(i)
            i += 1
        return res

print(Solution().findSubstring())