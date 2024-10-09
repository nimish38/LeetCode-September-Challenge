class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
print(Solution().isPalindrome(x = 121))