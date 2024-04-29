class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k %= n
        split, nums = nums[n - k:], nums[:n - k]
        nums = split + nums
        print(nums)

Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)
