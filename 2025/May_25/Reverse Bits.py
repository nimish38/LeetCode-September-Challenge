class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
            ans <<= 1
            if n & 1:
                ans |= 1
            n >>= 1
        return ans

print(Solution().reverseBits(43261596))