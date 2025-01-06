class Solution:
    def longestSubarray(self, nums):
        if len(nums) == 1:
            return 0

        start, end, zeros = 0, 0, 0
        for end in range(len(nums)):
            if not nums[end]:
                zeros += 1

            if zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1

        return end - start

print(Solution().longestSubarray([1,1,1]))