from collections import defaultdict
class Solution:
    def twoSum(self, nums, target: int):
        i, j =  0, len(nums) - 1
        ind = defaultdict(list)

        for k in range(len(nums)):
            ind[nums[k]].append(k)
        nums.sort()

        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                break

        if nums[i] == nums[j]:
            return ind[nums[i]]
        return [ind[nums[i]][0], ind[nums[j]][0]]

print(Solution().twoSum(nums = [3,2,3], target = 6))