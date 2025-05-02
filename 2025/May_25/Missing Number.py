class Solution:
    def missingNumber(self, nums) -> int:
        s, n = sum(nums), len(nums)
        return ((n * (n + 1)) // 2) - s

print(Solution().missingNumber(nums = [9,6,4,2,3,5,7,0,1]))