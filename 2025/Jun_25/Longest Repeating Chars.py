from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        freq, best, i, j, maxFreq = defaultdict(int), 0, 0, 0, 0
        while j < len(s):
            freq[s[j]] += 1
            maxFreq, length = max(maxFreq, freq[s[j]]),  j - i + 1
            if length - maxFreq <= k:
                best = max(best, j - i + 1)
            else:
                freq[s[i]] -= 1
                i += 1
                maxFreq = 0
            j += 1
        return best


