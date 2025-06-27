class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

print(Solution().rob(nums = [2,7,9,3,1]))