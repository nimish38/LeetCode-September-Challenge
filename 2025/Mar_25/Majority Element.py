class Solution(object):
    def majorityElement(self, nums):
        curr, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if curr == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    curr, cnt = nums[i], 1
        return curr