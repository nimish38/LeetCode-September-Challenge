from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        i, j, window, start = 0, 0, float('inf'), -1
        mapping, cnt = defaultdict(lambda: 0), len(t)

        for char in t:
            mapping[char] += 1

        while j < len(s):
            if mapping[s[j]] > 0:
                cnt -= 1
            mapping[s[j]] -= 1

            while cnt == 0:
                if j - i + 1 < window:
                    window = j - i + 1
                    start = i

                mapping[s[i]] += 1
                if mapping[s[i]] > 0:
                    cnt = 1
                i += 1
            j += 1

        return s[start: start + window]

print(Solution().minWindow(s = "ADOBCOAEBANIIIC", t = "ABC"))