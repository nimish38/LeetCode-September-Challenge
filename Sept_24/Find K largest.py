class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        l, r, pivot = 0, len(nums), 0
        while True:
            pivot = quick_select(l, r)
            if pivot == k - 1:
                break
            elif pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1

        return nums[pivot]

print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))