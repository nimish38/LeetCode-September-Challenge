import heapq


class Solution:
    def isPossible(self, target) -> bool:
        curr = sum(target)
        heapq._heapify_max(target)
        val = heapq._heappop_max(target)
        while val > 1:
            curr -= val
            if curr <= 0 or val <= curr:
                return False
            val = val % curr
            if val > 0:
                heapq.heappush(target, val)
            else:
                heapq.heappush(target, curr)
            curr += val
            heapq._heapify_max(target)
            val = heapq._heappop_max(target)
        return val == 1


print(Solution().isPossible(target = [5,2]))
