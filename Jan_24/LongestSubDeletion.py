class Solution:
    def longestSubarray(self, nums):
        if len(nums) == 1:
            return 0

        start, end, maxOnes = 0, 0, 0
        for end in range(len(nums)):
            maxOnes = max(end - start + 1, maxOnes)
            if not nums[end]:
                start += 1
        return maxOnes - 1

print(Solution().longestSubarray([1,0,0,1,1,0,1,1,1]))