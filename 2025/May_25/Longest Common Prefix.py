class Solution(object):
    def longestCommonPrefix(self, strs):
        def common(a, b):
            i = 0
            while i < min(len(a), len(b)) and a[i] == b[i]:
                i += 1
            return a[:i]

        if len(strs) == 1:
            return strs[0]
        x, i = common(strs[0], strs[1]), 2
        while x!= '' and i < len(strs):
            x = common(x, strs[i])
            i += 1
        return x

print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
