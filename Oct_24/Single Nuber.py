import functools, operator
class Solution:
    def singleNumber(self, nums) -> int:
        return functools.reduce(operator.xor, nums)

print(Solution().singleNumber(nums = [4,1,2,1,2]))