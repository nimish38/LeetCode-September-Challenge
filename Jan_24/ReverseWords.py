class Solution:
    def reverseWords(self, s: str) -> str:
        strList = list(s.split())
        return ' '.join(strList[::-1])

a = Solution()
print(a.reverseWords("a good   example"))