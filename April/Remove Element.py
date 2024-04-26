class Solution:
    def removeElement(self, nums, val):
        i, j, cnt = 0, len(nums) - 1, 0
        while i <= j:
            if i == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                cnt += 1
            else:
                i += 1
        print(nums)
        return len(nums) - cnt

print(Solution().removeElement(nums = [3,2,2,3], val = 3))
