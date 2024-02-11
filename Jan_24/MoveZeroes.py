class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        temp, cnt = [], 0
        for num in nums:
            if num != 0:
                temp.append(num)
            else:
                cnt += 1
        nums = temp.copy()
        nums.extend([0]*cnt)
        print(nums)

a = Solution()
a.moveZeroes([0,1,0,3,12])