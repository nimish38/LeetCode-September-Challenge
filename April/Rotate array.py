class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
        # print(nums)

Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)
