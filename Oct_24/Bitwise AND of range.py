class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for num in range(left + 1, right + 1):
            res = res & num
        return res

print(Solution().rangeBitwiseAnd(left = 5, right = 7))