class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(n)[::-1]
        return int(n, 10)