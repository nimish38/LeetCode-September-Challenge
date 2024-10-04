class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        return str(n).count('1')

print(Solution().hammingWeight(n = 11))