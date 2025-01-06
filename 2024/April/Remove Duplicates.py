class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        # print(nums)
        return j

print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
