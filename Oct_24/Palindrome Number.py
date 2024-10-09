class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        divisor = 1
        while x >= divisor:
            divisor *= 10
        divisor //= 10
        while x > 10:
            left, right = x // divisor, x % 10
            if left != right:
                return False
            x %= divisor
            x //= 10
            divisor //= 100
        return True

print(Solution().isPalindrome(x = 31213))