class Solution(object):
    def rotate(self, nums, k):
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k %= n
        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)

print(Solution().rotate(nums = [-1,-100,3,99], k = 2))