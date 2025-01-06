class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        pos = i
        while i>= 0 and s[i] != ' ':
            i -= 1
        return pos - i

print(Solution().lengthOfLastWord("lfy"))