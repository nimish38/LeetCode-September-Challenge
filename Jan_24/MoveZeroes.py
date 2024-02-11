class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, i = [], 0
        while i < len(nums):
            if nums[i] == 0:
                zero.append(i)
            else:
                if len(zero) > 0:
                    nums[zero[0]] = nums[i]
                    del zero[0]
                    nums[i] = 0
                    zero.append(i)
            i += 1
        print(nums)

a = Solution()
a.moveZeroes([0])