class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums = set(nums)
        best, curr = 0, 1
        for val in nums:
            if val - 1 in nums:
                continue
            curr = val
            while curr + 1 in nums:
                curr += 1
            best = max(best, curr - val + 1)
        return best

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))


