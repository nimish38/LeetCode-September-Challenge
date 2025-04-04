class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))