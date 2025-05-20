class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        carry = 1
        if n < 0:
            x = 1 / x
            n *= -1
        while n > 1:
            if n & 1:
                carry *= x
                n -= 1
            else:
                x *= x
                n >>= 1
        return x * carry

print(Solution().myPow(x = 2.00000, n = -2))