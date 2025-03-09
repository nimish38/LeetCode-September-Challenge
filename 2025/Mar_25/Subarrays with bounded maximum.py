class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        cnt, curr, i = 0, 0, 0
        for j in range(len(nums)):
            if nums[j] > right:
                curr, i = 0, j + 1
            elif left <= nums[j] <= right:
                curr = j - i + 1
            cnt += curr
        return cnt


print(Solution().numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))