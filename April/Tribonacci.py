class Solution:
    def tribonacci(self, n: int) -> int:
        T0, T1, T2 = 0, 1, 1

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            for i in range(3, n + 1):
                cnt = T0 + T1 + T2
                T0, T1, T2 = T1, T2, cnt
            return cnt

print(Solution().tribonacci(n = 25))