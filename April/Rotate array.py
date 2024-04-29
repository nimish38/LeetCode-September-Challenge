class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        if k > 0:
            reverse(0, n - k -1)
            reverse(n - k, n - 1)
            reverse(0, n - 1)
        print(nums)

Solution().rotate(nums = [1,2,3,4,5,6,7], k = 5)
