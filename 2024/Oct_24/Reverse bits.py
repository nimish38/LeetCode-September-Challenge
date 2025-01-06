class Solution:
    def reverseBits(self, n) -> int:
        n = format(n, 'b')
        n = ('0' * (32 - len(n))) + n
        n = n[::-1]
        return int(n, 2)

print(Solution().reverseBits(43261596))