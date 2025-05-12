class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        one_step, two_step, dest = 1, 2, 3

        for i in range(3, n + 1):
            dest = one_step + two_step
            one_step, two_step = two_step, dest

        return dest