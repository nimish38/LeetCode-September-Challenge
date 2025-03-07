class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs, n = [], len(profit)
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[0])
        memo = [-1] * n

        def solve(i):
            def findNextJob(i, target):
                j, res = n - 1, n
                while i <= j:
                    mid = (i + j) // 2
                    if jobs[mid][0] < target:
                        i = mid + 1
                    else:
                        res = mid
                        j = mid - 1
                return res
            if i >= len(profit):
                return 0
            if memo[i] == -1:
                next = findNextJob(i + 1, jobs[i][1])
                take = jobs[i][2] + solve(next)
                skip = solve(i + 1)
                memo[i] = max(take, skip)
            return memo[i]
        return solve(0)


print(Solution().jobScheduling(startTime = [6,15,7,11,1,3,16,2], endTime = [19,18,19,16,10,8,19,8], profit = [2,9,1,19,5,7,3,19]))