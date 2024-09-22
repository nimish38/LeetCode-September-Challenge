class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def quick_select(i, j):
            piv, x, i = nums[i], i, i + 1
            while i <= j:
                if nums[i] < piv < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                if nums[i] >= piv:
                    i += 1
                if nums[j] <= piv:
                    j -= 1
            nums[x], nums[j] = nums[j], nums[x]
            return j

        l, r, pivot = 0, len(nums) - 1, 0
        while True:
            pivot = quick_select(l, r)
            if pivot == k - 1:
                break
            elif pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1

        return nums[pivot]

print(Solution().findKthLargest(nums = [3], k = 1))