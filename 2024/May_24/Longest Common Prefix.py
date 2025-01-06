class Solution:
    def longestCommonPrefix(self, s) -> str:
        ans = ""
        s.sort()

        for i in range(min(len(s[0]), len(s[-1]))):
            if s[0][i] != s[-1][i]:
                return ans
            ans += s[0][i]
        return ans

print(Solution().longestCommonPrefix(s = ["flower","flow","flight"]))
