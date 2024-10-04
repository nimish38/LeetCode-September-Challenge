class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2 # 0 if rightmost bit is 0, 1 if rightmost bit is 1
            n = n >> 1 # shift right to the next bit
        return res

print(Solution().hammingWeight(n = 2147483645))