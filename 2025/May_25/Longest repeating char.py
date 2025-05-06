from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, maxfreq, best, cnt = 0, 0, 0, 0, defaultdict(int)
        while j < len(s):
            cnt[s[j]] += 1
            maxfreq = max(maxfreq, cnt[s[j]])
            length = j - i + 1
            if length - maxfreq <= k:
                best = max(best, length)
            else:
                cnt[s[i]] -= 1
                i += 1
                maxfreq = 0
            j += 1
        return best

print(Solution().characterReplacement(s = "AABABBA", k = 1))

