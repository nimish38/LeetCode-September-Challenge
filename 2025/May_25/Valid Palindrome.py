class Solution(object):
    def isPalindrome(self, s):
        t = ''
        for c in s:
            if c.isalnum():
                t += c.lower()
        return t == t[::-1]

print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))