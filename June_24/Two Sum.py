class Solution:
    def twoSum(self, nums, target: int):
        i, j =  0, len(nums) - 1
        nums.sort()
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [i, j]

print(Solution().twoSum(nums = [2,7,11,15], target = 13))