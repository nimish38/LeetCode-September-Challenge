class Solution:
    def minFlips(self, a: int, b: int, c: int):
        xor = (a | b) ^ c
        singles = xor & (a & b)
        return bin(singles).count('1') + bin(xor).count('1')

print(Solution().minFlips(a = 2, b = 6, c = 5))