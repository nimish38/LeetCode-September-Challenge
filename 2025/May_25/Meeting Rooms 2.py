class Solution:
    def minMeetingRooms(self, intervals) -> int:
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)
        i, j, cnt, best = 0, 0, 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                cnt += 1
                best = max(cnt, best)
                i += 1
            else:
                cnt -= 1
                j += 1
        return best

