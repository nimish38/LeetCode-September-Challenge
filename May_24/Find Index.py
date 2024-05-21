class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle) - 1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i + 1: i + n] == needle[1:]:
                    return i

        return -1
