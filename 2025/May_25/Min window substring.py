from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        curr, req, i, j, best, ans = defaultdict(int), len(t), 0, 0, float('inf'), ''

        for c in t:
            curr[c] += 1

        while j < len(s):
            curr[s[j]] -= 1
            if curr[s[j]] >= 0:
                req -= 1
                if req == 0:
                    if j + 1 - i < best:
                        best, ans = j - i + 1, s[i: j+ 1]
                while i <= j and req == 0:
                    curr[s[i]] += 1
                    if curr[s[i]] > 0:
                        req = 1
                    if j + 1 - i < best:
                        best, ans = j - i + 1, s[i: j + 1]
                    i += 1
            j += 1
        return ans

print(Solution().minWindow(s = "AA", t = "AA"))