class Solution(object):
    def longestConsecutive(self, nums):
        nums, best = set(nums), 0
        for elem in nums:
            if elem - 1 in nums:
                continue
            curr, num = 1, elem
            while num + 1 in nums:
                curr += 1
                num += 1
            best = curr if curr > best else best
        return best


print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))