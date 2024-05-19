class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

print(Solution().reverseWords(s = "the sky is blue"))