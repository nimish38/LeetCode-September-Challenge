import heapq


class Solution:
    def isPossible(self, target) -> bool:
        curr = sum(target)
        heapq._heapify_max(target)
        val = heapq._heappop_max(target)
        while val > 1:
            curr -= val
            if curr <= 0 or (val - curr) <= 0:
                return False
            heapq.heappush(target, val - curr)
            val = heapq._heappop_max(target)
        return val == 1


print(Solution().isPossible(target = [9,3,5]))
