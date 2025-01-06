class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        ptr = 0
        for i in range(len(s)):
            if s[i] == '*':
                ptr -= 1
            else:
                s[ptr] = s[i]
                ptr += 1
        s = ''.join(s)
        return s[:ptr]

print(Solution().removeStars("erase*****"))