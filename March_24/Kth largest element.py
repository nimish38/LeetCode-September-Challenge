class Solution:
    def findKthLargest(self, nums, k):
        def QuickSelect(i, j):
            pivot = i
            i += 1
            while i <= j:
                if nums[i] < nums[pivot] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                if nums[i] >= nums[pivot]:
                    i += 1
                if nums[j] <= nums[pivot]:
                    j -= 1
            nums[pivot], nums[j] = nums[j], nums[pivot]
            return j

        left, right, pivot_index = 0, len(nums) - 1, 0
        while True:
            pivot_index = QuickSelect(left, right)
            if pivot_index == k - 1:
                return nums[pivot_index]
            elif pivot_index < k - 1:
                left = pivot_index + 1
            else:
                right = pivot_index - 1



# print(Solution().findKthLargest(nums = [1], k = 1))