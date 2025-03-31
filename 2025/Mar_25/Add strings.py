import sys


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(50000)
        return str(int(num1)+int(num2))


print(Solution().addStrings(num1 = "11", num2 = "123"))