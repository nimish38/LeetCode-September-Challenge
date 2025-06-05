class Solution(object):
    def isPalindrome(self, s):
        pal = ''
        for c in s:
            val = ord(c)
            if 65 <= val <= 90:
                pal += chr(val + 32)
            elif 97 <= val <= 122 or 48 <= val <= 57:
                pal += chr(val)
        return pal == pal[::-1]