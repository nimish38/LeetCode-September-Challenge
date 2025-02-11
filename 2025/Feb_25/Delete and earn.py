from collections import Counter


class Solution:
    def deleteAndEarn(self, nums) -> int:
        cnt , n = Counter(nums), len(nums)
        nums = sorted(list(set(nums)))

        def solve(i):
            if i >= n:
                return 0
            take = nums[i] * cnt[nums[i]]
            if i < n - 1 and nums[i] != nums[i + 1] - 1:
                take += solve(i + 1)
            else:
                take += solve(i + 2)
            skip = solve(i + 1)
            return max(take, skip)

        return solve(0)


print(Solution().deleteAndEarn(nums = [3,4,2]))