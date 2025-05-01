class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if not s:
            return 0
        chars, i, j, best = {s[0]: 1}, 0, 1, 1
        while j < len(s):
            if s[j] not in chars:
                chars[s[j]] = 1
                j += 1
                best = max(best, len(chars))
            else:
                del chars[s[i]]
                i += 1
        return best

print(Solution().lengthOfLongestSubstring(s = ""))