class Solution:
    def longestCommonPrefix(self, strs):
        lcp = strs[0]
        for i in range(1, len(strs)):
            curr = strs[i]
            j = 0
            while j < min(len(lcp), len(curr)) and lcp[j] == curr[j]:
                j += 1
            if j == 0:
                return ""
            lcp = lcp[:j]
        return lcp


