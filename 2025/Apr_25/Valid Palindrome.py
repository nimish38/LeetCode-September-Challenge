class Solution:
    def isPalindrome(self, s: str) -> bool:
        s, temp = s.lower(), ''
        for c in s:
            if c.isalnum():
                temp += c
        return temp == temp[::-1]


print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
