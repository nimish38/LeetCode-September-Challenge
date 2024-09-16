class Solution:
    def search(self, nums, target: int):
        if target in nums:
            return nums.index(target)
        return -1

print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0))
