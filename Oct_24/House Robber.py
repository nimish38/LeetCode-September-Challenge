class Solution:
    def rob(self, nums) -> int:
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        #
        # amt = [-1]*(n + 1)
        # amt[0], amt[1] = 0, nums[0]
        #
        # for i in range(2, n + 1):
        #     amt[i] = max(amt[i - 1], amt[i - 2] + nums[i - 1])
        # return amt[n]

        n = len(nums)
        amt = [-1] * (n)

        def solve(ind):
            if ind >= n:
                return 0
            if amt[ind] == -1:
                incl = solve(ind + 2) + nums[ind]
                excl = solve(ind + 1)
                amt[ind] = max(incl, excl)
            return amt[ind]

        return solve(0)


print(Solution().rob(nums = [2,7,9,3,1]))