class Solution:
    def sortColors(self, nums) -> None:
        zero, one, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1

        for i in range(n):
            if zero > 0:
                nums[i] = 0
                zero -= 1
            elif one > 0:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2
        return nums


print(Solution().sortColors(nums = [2,0,2,1,1,0]))