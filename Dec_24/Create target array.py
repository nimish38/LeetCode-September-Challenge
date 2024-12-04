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
            curr += val - curr
            heapq._heapify_max(target)
            val = heapq._heappop_max(target)
        return val == 1


print(Solution().isPossible(target = [5,2]))
