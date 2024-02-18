class Solution:
    def longestOnes(self, nums, k):
        maxOnes = curOnes = 0
        threshold = k
        for num in nums:
            if num:
                curOnes += 1
            else:
                if threshold > 0:
                    curOnes += 1
                    threshold -= 1
                else:
                    curOnes = 1
                    threshold = k - 1
            if curOnes > maxOnes:
                maxOnes = curOnes
        return maxOnes

print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))