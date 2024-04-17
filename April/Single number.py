class Solution:
    def singleNumber(self, nums):
        for num in set(nums):
            if nums.count(num) == 1:
                return num

print(Solution().singleNumber(nums = [4,1,2,1,2]))