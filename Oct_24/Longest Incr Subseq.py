class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, last = len(nums), float('-inf')

        def solve(ind, last):
            if ind == n:
                return 0
            take = 0
            if nums[ind] > last:
                take = 1 + solve(ind + 1, nums[ind])
            skip = solve(ind + 1, last)
            return max(take, skip)

        return solve(0, last)

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))