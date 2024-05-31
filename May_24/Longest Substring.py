class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, curr = 1, set(s[0])
        i, j = 0, 1

        while j < len(s):
            if s[j] not in curr:
                curr.add(s[j])
            else:
                curr.remove(s[i])
                curr.add(s[j])
                i += 1
            res = max(res, len(curr))
            j += 1
        return res

print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))