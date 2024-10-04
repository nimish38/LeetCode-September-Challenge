class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[1:]
        return n.count('1')

print(Solution().hammingWeight(n = 2147483645))