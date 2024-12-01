class Solution:
    def sortColors(self, nums) -> None:
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 1:
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums
    

print(Solution().sortColors(nums = [2,0,2,1,1,0]))