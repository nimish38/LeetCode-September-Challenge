class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        ind = {}
        for i in range(len(nums)):
            if nums[i] in ind and i - ind[nums[i]] <= k:
                return True
            ind[nums[i]] = i
        return False

print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 2))
