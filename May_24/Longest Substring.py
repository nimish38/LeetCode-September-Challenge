class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, curr = 1, set(s[0])
        i, j = 0, 1

        while j < len(s):
            if s[j] not in curr:
                curr.add(s[j])
            else:
                curr.remove(s[i])
                i += 1
            j += 1
        return j - i

print(Solution().lengthOfLongestSubstring())