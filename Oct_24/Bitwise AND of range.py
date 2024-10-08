class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1 #n & n-1 removes set bit
        return right

print(Solution().rangeBitwiseAnd(left = 5, right = 7))
