from collections import Counter


class Solution:
    def deleteAndEarn(self, nums) -> int:
        cnt = Counter(nums)
        nums = sorted(list(set(nums)))
        n, prev1, prev2, ans = len(nums), 0, 0, 0

        for i in range(n):
            curr = nums[i] * cnt[nums[i]]
            if i > 0 and nums[i] != nums[i - 1] + 1:
                curr = curr + prev1
            else:
                curr = max(curr + prev2, prev1)
            ans = max(ans, curr)
            prev2, prev1 = prev1, curr
        return ans


print(Solution().deleteAndEarn(nums = [2,2,3,3,3,4]))