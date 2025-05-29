class Solution:
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            if rev > (INT_MAX - digit) // 10:
                return 0
            rev = rev * 10 + digit
        return sign * rev