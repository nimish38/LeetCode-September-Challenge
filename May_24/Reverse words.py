class Solution:
    def reverseWords(self, s: str) -> str:
        res, i, curr = '', len(s) - 1, ''

        while i >= 0:
            if s[i] == ' ':
                if len(curr):
                    res += curr + ' '
                    curr = ''
                else:
                    i -= 1
                    continue
            else:
                curr = s[i] + curr
            i -= 1

        if curr:
            res += curr

        return res

print(Solution().reverseWords(s = "  hello world  "))