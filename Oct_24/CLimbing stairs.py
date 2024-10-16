class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(x):
            if x < 0:
                return 0
            if x == 0:
                return 1
            return solve(x - 1) + solve(x-2)
        return solve(n)

print(Solution().climbStairs())