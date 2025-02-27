class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        res = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        return res


print(Solution().maximumProduct(nums = [-8,-7,3,4]))