class Solution:
    def removeStars(self, s: str) -> str:
        new_str = ''
        for char in s:
            if char == '*':
                new_str = new_str[:-1]
            else:
                new_str += char
        return new_str

print(Solution().removeStars("leet**cod*e"))