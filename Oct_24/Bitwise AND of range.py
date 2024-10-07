class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for num in range(left + 1, right + 1):
            res = res & num
            if res == 0:
                return 0
        return res

print(Solution().rangeBitwiseAnd(left = 1, right = 2147483647))