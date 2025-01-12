from collections import defaultdict


class Solution:
    def twoSum(self, nums, target: int):
        val = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in val:
                return [val[target - nums[i]], i]
            else:
                val[nums[i]] = i


print(Solution().twoSum(nums = [3,2,4], target = 6))