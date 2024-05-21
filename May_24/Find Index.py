class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        if n > len(haystack):
            return -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                # print(haystack[i + 1: i + n], needle[1:])
                if haystack[i + 1: i + n] == needle[1:]:
                    return i
        return -1

print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
