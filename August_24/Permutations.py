import itertools
class Solution:
    def permute(self, nums):
        x = map(list, itertools.permutations(nums))
        return list(x)

print(Solution().permute(nums = [1,2,3]))