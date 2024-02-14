class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        i, cnt, j = 0, 0, len(nums) - 1
        while j >= 0 and nums[j] >= k:
            j -= 1
        while i < j:
            if nums[i] + nums[j] == k:
                cnt += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return cnt

print(Solution().maxOperations([1,2,3,4], 5))
