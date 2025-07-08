class Solution(object):
    def removeElement(self, nums, val):
        ind = 0
        for num in nums:
            if num != val:
                nums[ind] = num
                ind += 1
        return ind

print(Solution().removeElement(nums = [3,2,2,3], val = 3))