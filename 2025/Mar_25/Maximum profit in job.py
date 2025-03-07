class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = []
        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[0])

        def solve(i, minStart):
            if i >= len(profit):
                return 0
            take, skip = 0, 0
            if jobs[i][0] >= minStart:
                take = jobs[i][2] + solve(i + 1, jobs[i][1])
            skip = solve(i + 1, minStart)
            return max(take, skip)
        return solve(0, 0)


print(Solution().jobScheduling(startTime = [6,15,7,11,1,3,16,2], endTime = [19,18,19,16,10,8,19,8], profit = [2,9,1,19,5,7,3,19]))