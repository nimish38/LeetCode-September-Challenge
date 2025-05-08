class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        curr_st, curr_end = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            s_st, s_end = intervals[i]
            if curr_end >= s_st:
                curr_end = max(curr_end, s_end)
            else:
                res.append([curr_st, curr_end])
                curr_st, curr_end = s_st, s_end
        res.append([curr_st, curr_end])
        return res

print(Solution().merge(intervals = [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]))