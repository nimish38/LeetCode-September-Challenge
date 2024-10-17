class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [-1]*(n+1)
        steps[1] = 1
        steps[0] = 0
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]

print(Solution().climbStairs(4))