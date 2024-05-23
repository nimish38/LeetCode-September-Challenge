class Solution:
    def isPalindrome(self, s: str) -> bool:
        s, t = s.lower(), ''
        for char in s:
            if 96 < ord(char) < 123 or 47 < ord(char) < 58:
                t += char
        if len(t) < 2:
            return True
        i, j = 0, len(t) - 1
        while i < j and t[i] == t[j]:
            i += 1
            j -= 1
        if i < j:
            return False
        return True



print(Solution().isPalindrome(s = "0P"))