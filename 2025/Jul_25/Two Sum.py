class Solution(object):
    def twoSum(self, nums, target):
        last = {}
        for i in range(len(nums)):
            if nums[i] in last:
                return [last[nums[i]], i]
            last[target - nums[i]] = i
        return [-1, -1]