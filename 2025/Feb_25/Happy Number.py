class Solution:
    def isHappy(self, n: int) -> bool:
        prev = {}
        while True:
            if n == 1:
                return True
            if n in prev:
                return False
            prev[n], s, n = 1, str(n), 0
            for c in s:
                n += int(c) ** 2


print(Solution().isHappy(n = 2))