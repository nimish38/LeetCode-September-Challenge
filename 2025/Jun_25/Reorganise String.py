import heapq
from collections import Counter


class Solution(object):
    def reorganizeString(self, s):
        chars, arr, res = Counter(s), [], ''
        for c in chars:
            heapq.heappush(arr, (-chars[c], c))

        while arr:
            f, c = heapq.heappop(arr)
            if res and c == res[-1]:
                if not arr:
                    return ''
                sec_f, sec_c = heapq.heappop(arr)
                res += sec_c
                if sec_f < -1:
                    heapq.heappush(arr, (sec_f + 1, sec_c))
                heapq.heappush(arr, (f, c))
            else:
                res += c
                if f < -1:
                    heapq.heappush(arr, (f + 1, c))
        return res

print(Solution().reorganizeString(s = 'aab'))