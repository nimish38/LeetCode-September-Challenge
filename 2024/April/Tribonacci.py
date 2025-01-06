class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        T0, T1, T2 = 0, 1, 1
        for i in range(n - 2):
            T0, T1, T2 = T1, T2, T0 + T1 + T2
        return T2

print(Solution().tribonacci(n = 25))