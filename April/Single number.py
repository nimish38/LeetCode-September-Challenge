import functools
import operator
class Solution:
    def singleNumber(self, nums):
        return functools.reduce(operator.xor, nums)

print(Solution().singleNumber(nums = [4,4,2,1,2]))