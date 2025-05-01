class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        best, curr = 0, 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                curr += 1
            else:
                best, curr = max(best, curr), 1
        return max(best, curr)

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))


