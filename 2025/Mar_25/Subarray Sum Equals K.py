class Solution:
    def subarraySum(self, nums, k: int) -> int:
        i, j, curr, cnt = 0, 0, 0, 0
        while j < len(nums):
            curr += nums[j]
            if curr == k:
                cnt += 1
                j += 1
            elif curr < k:
                j += 1
            else:
                while curr > k:
                    curr -= nums[i]
                    i += 1
                if curr == k:
                    cnt += 1
                j += 1
        return cnt


print(Solution().subarraySum(nums = [1,2,2,3,1,2,1,4], k = 4))