class Solution:
    def majorityElement(self, nums):
        candidate, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                cnt += 1
            else:
                if cnt == 0:
                    candidate = nums[i]
                cnt -= 1
        return candidate


print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))
