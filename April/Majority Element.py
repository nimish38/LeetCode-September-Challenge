class Solution:
    def majorityElement(self, nums):
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        for key in cnt.keys():
            if cnt[key] > len(nums) // 2:
                return key

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))
