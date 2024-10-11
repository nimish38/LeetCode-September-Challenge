import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 1
        n, res = math.factorial(n), 0
        while n%10 == 0:
            res += 1
            n //= 10
        return res

print(Solution().trailingZeroes(n = 5))