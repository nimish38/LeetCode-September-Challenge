class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [-1]*(n+1)
        steps[0] = 1

        def solve(x):
            if x < 0:
                return 0
            if x == 0:
                return 1
            if steps[x] == -1:
                steps[x] = solve(x-1) + solve(x-2)
            return steps[x]

        return solve(n)

print(Solution().climbStairs(3))