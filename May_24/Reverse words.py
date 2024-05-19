class Solution:
    def reverseWords(self, s: str) -> str:
        res, i, curr = '', len(s) - 1, ''

        while i >= 0:
            if s[i] == ' ':
                if curr:
                    res += ' ' + curr
                    curr = ''
                else:
                    continue
            else:
                curr = s[i] + curr
            i -= 1

        if curr:
            res += ' ' + curr

print(Solution().reverseWords(s = "the sky is blue"))