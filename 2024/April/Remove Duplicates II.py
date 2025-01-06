class Solution:
    def removeDuplicates(self, nums):
        j = 2
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1] or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))