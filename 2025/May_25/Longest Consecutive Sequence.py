class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        best, curr = 0, 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                curr += 1
            else:
                best, curr = max(best, curr), 1
        return max(best, curr)

print(Solution().longestConsecutive(nums = []))


