class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        def solve(i, minStart):
            if i >= len(profit):
                return 0
            take, skip = 0, 0
            if startTime[i] >= minStart:
                take = profit[i] + solve(i + 1, endTime[i])
            skip = solve(i + 1, minStart)
            return max(take, skip)
        return solve(0, 0)


print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))