import itertools
class Solution:
    def findSubstring(self, s: str, words):
        combo = list(itertools.permutations(words))
        perms = []
        for lis in combo:
            perms.append(''.join(lis))

        i, n, res = 0, len(perms[0]), []
        while i < len(s) - n + 1:
            # print(s[i: i + n])
            if s[i: i + n] in perms:
                res.append(i)
            i += 1
        return res

print(Solution().findSubstring(s = "barfoothefoobar", words = ["foo","bar"]))