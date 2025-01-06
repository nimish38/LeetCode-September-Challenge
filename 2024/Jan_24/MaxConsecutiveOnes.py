class Solution:
    def longestOnes(self, nums, k):
        start, end, zeros = 0, 0, 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1

            if zeros > k:
                if not nums[start]:
                    zeros -= 1
                start += 1

        return end - start + 1


print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))