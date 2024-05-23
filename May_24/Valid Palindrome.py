class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for char in s:
            asci = ord(char)
            if 64 < asci < 91 or 47 < asci < 58:
                t += char
            if 96 < asci < 123:
                t += chr(asci - 32)
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