class Solution:
    def sortColors(self, nums) -> None:
        zero, one, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
        nums = [0]*zero + [1]*one + [2]*(n - zero - one)
        return nums

