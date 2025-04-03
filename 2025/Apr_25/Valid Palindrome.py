class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i > j:
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
            elif s[i] == s[j]:
                return False
        return True
