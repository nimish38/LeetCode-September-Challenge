class Solution:
    def removeElement(self, nums, val):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt


print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
