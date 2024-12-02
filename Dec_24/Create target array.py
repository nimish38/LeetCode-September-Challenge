import heapq


class Solution:
    def isPossible(self, target) -> bool:
        n, curr, mini = len(target), len(target), 1
        heapq.heapify(target)

        while len(target) > 0:
            x = heapq.heappop(target)
            if curr > x:
                return False
            elif curr < x:
                heapq.heappush(target, x)
            curr += curr - mini

        if len(target) == 0:
            return True
        return False


print(Solution().isPossible(target = [9,3,5]))
