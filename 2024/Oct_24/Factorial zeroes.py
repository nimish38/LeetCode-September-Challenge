class Solution:
    def trailingZeroes(self, n: int) -> int:
        div, res = 5, 0
        while div <= n:
            res += n // div
            div *= 5
        return res

print(Solution().trailingZeroes(n = 150))