import heapq


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        leftmax, rightmin = [], []

        def make_heap(arr):
            for val in arr:
                if len(leftmax) == 0:
                    heapq.heappush(leftmax, -1 * val)

                elif val > (-1 * leftmax[0]):
                    heapq.heappush(rightmin, val)
                    if len(rightmin) > len(leftmax):
                        pop = heapq.heappop(rightmin)
                        heapq.heappush(leftmax, -1 * pop)

                else:
                    heapq.heappush(leftmax, -1 * val)
                    if len(leftmax) - len(rightmin) > 1:
                        pop = heapq.heappop(leftmax)
                        heapq.heappush(rightmin, -1 * pop)

        make_heap(nums1)
        make_heap(nums2)
        if (m + n) % 2:
            return -1 * leftmax[0]
        else:
            return ((-1* leftmax[0]) + rightmin[0]) / 2


print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))