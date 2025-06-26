class Solution(object):
    def removeDuplicates(self, nums):
        unique, ind = {}, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[ind] = nums[i]
                ind += 1
        return ind

print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
