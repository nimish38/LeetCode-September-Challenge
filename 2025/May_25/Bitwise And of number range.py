class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        moves = 0
        while left != right:
            left >>= 1
            right >>= 1
            moves += 1
        return left << moves

print(Solution().rangeBitwiseAnd(left = 5, right = 7))