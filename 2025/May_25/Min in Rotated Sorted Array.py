class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r, res = 0, len(nums) - 1, float('inf')
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            else:
                mid = (l + r) // 2
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                res = min(res, nums[mid])
        return res

print(Solution().findMin(nums =  [2, 1]))