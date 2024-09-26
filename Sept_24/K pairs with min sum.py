import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap, m, n = [], len(nums1) - 1, len(nums2) - 1
        heapq.heappush(heap, (nums1[0] + nums2[0], [0, 0]))
        vis, res = {(0, 0)}, []

        while k > 0:
            sum, val = heapq.heappop(heap)
            res.append([nums1[val[0]], nums2[val[1]]])
            k -= 1

            if val[0] < m and (val[0] + 1, val[1]) not in vis:
                sum_new = nums1[val[0] + 1] + nums2[val[1]]
                heapq.heappush(heap, (sum_new, [val[0] + 1, val[1]]))
                vis.add((val[0] + 1, val[1]))

            if val[1] < n and (val[0], val[1] + 1) not in vis:
                sum_new = nums1[val[0]] + nums2[val[1] + 1]
                heapq.heappush(heap, (sum_new, [val[0], val[1] + 1]))
                vis.add((val[0], val[1] + 1))

        return res


print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))