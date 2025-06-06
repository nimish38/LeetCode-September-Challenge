import heapq


class Solution(object):
    def longestDiverseString(self, a, b, c):
        arr, res = [], ''
        if a > 0:
            arr.append((-1 * a, 'a'))
        if b > 0:
            arr.append((-1 * b, 'b'))
        if c > 0:
            arr.append((-1 * c, 'c'))
        heapq.heapify(arr)

        while arr:
            freq, char = heapq.heappop(arr)
            if len(res) < 2:
                res += char
                if freq < -1:
                    heapq.heappush(arr, (freq + 1, char))
            else:
                if char == res[-1] and res[-2] == char:
                    if not arr:
                        return res
                    Fillerfreq, filler  = heapq.heappop(arr)
                    res += filler
                    if Fillerfreq < -1:
                        heapq.heappush(arr, (Fillerfreq + 1, filler))
                    heapq.heappush(arr, (freq, char))
                else:
                    res += char
                    if freq < -1:
                        heapq.heappush(arr, (freq + 1, char))
        return res

print(Solution().longestDiverseString(a = 1, b = 1, c = 7))