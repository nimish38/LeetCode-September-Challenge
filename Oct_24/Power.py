class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x * x, (n-1)//2)

print(Solution().myPow(x = 2.10000, n = 3))