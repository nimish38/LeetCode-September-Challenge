class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            if nums[l] > nums[mid]:
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

print(Solution().search(nums = [1,3], target = 3))