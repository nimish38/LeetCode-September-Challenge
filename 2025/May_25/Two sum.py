class Solution:
    def twoSum(self, nums, target: int):
        hash = {}
        for i ,c in enumerate(nums):
            hash[c] = i
        for i in range(len(nums)):
            if target - nums[i] in hash and i != hash[target - nums[i]]:
                return [i, hash[target - nums[i]]]
        return None

print(Solution().twoSum(nums = [2,7,11,15], target = 9))