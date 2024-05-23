class Solution:
    def isPalindrome(self, s: str) -> bool:
        s,t = s.lower(), ''
        for char in s:
            if char.isalnum():
                t += char
        if t == t[::-1]:
            return True
        return False

print(Solution().isPalindrome(s = "0Pananap"))